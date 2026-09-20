import json
import logging
import pandas as pd

from fastapi import UploadFile

from app.daos.task import TaskDAO
from app.models import Task, TaskStatus
from app.utils.minio import get_file
from app.utils.exception_handler import BizException
from app.utils.rule_engine import MaskEngine

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


class TaskPreviewCommand:
    def __init__(self, task: Task, rules: dict):
        self._task = task
        self._rules = rules

    async def run(self):
        await self.validate()
        await TaskDAO.upsert_mask_rule(self._task, self._rules)
        with get_file(f"{self._task.task_id}/analysis/sample.json") as obj:
            sample_data = json.loads(obj.read().decode("utf-8"))
            df = pd.DataFrame(sample_data)
            preview_data = MaskEngine().apply_dataframe(df, self._rules)
            logger.info(preview_data)
        return {}

    async def validate(self):
        with get_file(f"{self._task.task_id}/analysis/header.json") as obj:
            headers = json.loads(obj.read().decode("utf-8"))

        rule_headers = list(k for k in self._rules)
        if set(headers) != set(rule_headers):
            raise BizException("Wrong rule headers")
