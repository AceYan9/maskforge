from app.celery_app import celery_app, BaseTask
from app.models import Task
from app.utils.file_analyze import FileAnalyzer
from app.utils.minio import submit_analysis_data
from app.utils.rule_analyze import RuleAnalyzer


class ProcessFileTask(BaseTask):

    async def run_async(self, task_id):

        await self.init_db()

        task = await Task.get_or_none(
            task_id=task_id
        )

        if not task:
            return

        analyzer = FileAnalyzer(task.source_object, task.file_type)
        result = await analyzer()
        samples = result["samples"]

        task.total_rows = result["rows"]
        task.total_columns = result["columns"]
        await task.save()

        await submit_analysis_data(task_id, samples, "sample.json")

        rule_analyzer = RuleAnalyzer(samples, result["headers"])
        recommended_rule = await rule_analyzer()
        await submit_analysis_data(task_id, recommended_rule, "recommended_rule.json")


process_file = celery_app.register_task(ProcessFileTask())
