import json
import random
import logging
import pandas as pd

from fastapi import UploadFile

from app.daos.task import TaskDAO, TaskRunDAO
from app.models import Task, TaskStatus
from app.utils.s3 import get_file
from app.utils.exception_handler import BizException
from app.utils.rule_engine import MaskEngine
from app.utils.common import random_second, to_seconds
from app.utils.const import DATE_FORMATS, TIME_FORMATS, DATE_TIME_FORMATS

logger = logging.getLogger(__name__)


class TaskCreateCommand:
    def __init__(self, file: UploadFile):
        self._file = file

    async def run(self) -> str:
        await self.validate()
        return await TaskDAO.create_task(self._file)

    async def validate(self):
        pass


class TaskDetailCommand:
    def __init__(self, task: Task):
        self._task = task

    async def run(self):
        await self.validate()
        if self._task.status != TaskStatus.READY:
            return {"status": self._task.status}

        return await TaskDAO.get_task_detail(self._task)

    async def validate(self):
        pass


class TaskRuleCommand:
    def __init__(self, task: Task, rules: dict):
        self._task = task
        self._rules = rules

    async def validate(self):
        with get_file(f"{self._task.task_id}/analysis/header.json") as obj:
            headers = json.loads(obj.read().decode("utf-8"))

        rule_headers = list(k for k in self._rules)
        if not set(rule_headers).issubset(set(headers)):
            raise BizException("Wrong rule headers")

        for _, rule in self._rules.items():
            if rule.get("rule_type") == "date_offset_mask":
                date_format = rule.get("format")
                if date_format not in DATE_FORMATS + DATE_TIME_FORMATS:
                    raise BizException("Wrong date format")
                config_key = "date_offset"
                if not (date_offset := rule.get(config_key)):
                    raise BizException(f"Lack of {config_key} config")
                if (min_v := date_offset.get("min")) is None or (max_v := date_offset.get("max") ) is None:
                    raise BizException(f"Error {config_key} config")
                if min_v > max_v:
                    raise BizException("The minimum value cannot be greater than the maximum value")
                rule[f"{config_key}_val"] = random.randint(min_v, max_v)
            elif rule.get("rule_type") == "time_offset_mask":
                time_format = rule.get("format")
                if time_format not in TIME_FORMATS:
                    raise BizException("Wrong time format")
                config_key = "time_offset"
                if not (time_offset := rule.get(config_key)):
                    raise BizException(f"Lack of {config_key} config")
                if (min_v := time_offset.get("min")) is None or (max_v := time_offset.get("max") ) is None:
                    raise BizException(f"Error {config_key} config")
                if to_seconds(min_v) > to_seconds(max_v):
                    raise BizException("The minimum value cannot be greater than the maximum value")
                rule[f"{config_key}_val"] = random_second(min_v, max_v)


class TaskPreviewCommand(TaskRuleCommand):

    async def run(self):
        await self.validate()
        await TaskDAO.upsert_mask_rule(self._task, self._rules)
        with get_file(f"{self._task.task_id}/analysis/sample.json") as obj:
            sample_data = json.loads(obj.read().decode("utf-8"))
            df = pd.DataFrame(sample_data)
            preview_data = MaskEngine().apply_dataframe(df, self._rules)
        return preview_data.to_dict(orient="records")


class TaskRunCommand(TaskRuleCommand):

    async def run(self):
        await self.validate()
        run_id = await TaskRunDAO.create_task_run(self._task.task_id, self._rules)
        return run_id


class TaskRunListCommand:
    def __init__(self, task_id: str, page: int, page_size: int):
        self._task_id = task_id
        self._page = page
        self._page_size = page_size

    async def run(self):
        return await TaskRunDAO.get_run_list(self._task_id, self._page, self._page_size)
