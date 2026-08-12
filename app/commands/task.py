import logging

from fastapi import UploadFile

from app.daos.task import TaskDAO
from app.models import Task, TaskStatus

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
        logger.info(f"{self._task.status=}")
        if self._task.status != TaskStatus.READY:
            return {"status": self._task.status}

        return await TaskDAO.get_task_detail(self._task)

    async def validate(self):
        pass
