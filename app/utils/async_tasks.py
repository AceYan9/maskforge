import logging
import pandas as pd
from io import BytesIO
from pathlib import PurePosixPath

from app.celery_app import celery_app, BaseTask
from app.models import Task, TaskStatus, TaskRun, TaskRunStatus
from app.utils.file_analyze import FileAnalyzer
from app.utils.s3 import submit_analysis_data, get_file, upload_run_result
from app.utils.rule_analyze import RuleAnalyzer
from app.utils.rule_engine import MaskEngine

logger = logging.getLogger(__name__)


class ProcessFileTask(BaseTask):

    async def run_async(self, task_id):
        await self.init_db()

        task = await Task.get_or_none(task_id=task_id)
        if not task:
            return

        task.status = TaskStatus.ANALYZING
        await task.save()

        analyzer = FileAnalyzer(task.source_object, task.file_type)
        result = await analyzer()
        samples = result["samples"]
        headers = result["headers"]

        task.total_rows = result["rows"]
        task.total_columns = result["columns"]

        await submit_analysis_data(task_id, samples, "sample.json")
        await submit_analysis_data(task_id, headers, "header.json")

        rule_analyzer = RuleAnalyzer(samples, headers)
        recommended_rule = await rule_analyzer()
        await submit_analysis_data(task_id, recommended_rule, "recommended_rule.json")

        task.status = TaskStatus.READY
        await task.save()


class MaskRunTask(BaseTask):

    def _read_dataframe(self, s3_obj, file_type: str):
        data = BytesIO(s3_obj.read())

        if file_type == "csv":
            return pd.read_csv(
                data,
                encoding="utf-8-sig",
            )

        if file_type in {"xls", "xlsx"}:
            return pd.read_excel(
                data,
                engine="openpyxl" if file_type == "xlsx" else None,
            )

        raise ValueError(f"Unsupported file type: {file_type}")

    async def run_async(self, run_id):
        await self.init_db()
        # Ensure that the rule is successfully registered
        from app.utils import rules

        if not (task_run := await TaskRun.get_or_none(run_id=run_id)) or not (task_id := task_run.task_id):
            return
        if not (task := await Task.get_or_none(task_id=task_id)):
            return

        try:
            source_object = task.source_object
            file_type = PurePosixPath(source_object).suffix.lower().lstrip(".")
            with get_file(source_object) as obj:
                df = self._read_dataframe(obj, file_type)
                preview_data = MaskEngine().apply_dataframe(df, task_run.rules)
                await upload_run_result(task_id, preview_data, f"{run_id}.xlsx")
        except Exception as e:
            logger.error(f"Task run failed, run_id = {run_id}, task_id = {task_id}, error = {str(e)}")
            task_run.status = TaskRunStatus.FAILED
        else:
            task_run.status = TaskRunStatus.SUCCESS
        finally:
            await task_run.save()


process_file = celery_app.register_task(ProcessFileTask())
mask_run = celery_app.register_task(MaskRunTask())
