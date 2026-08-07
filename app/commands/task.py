from fastapi import UploadFile

from app.daos.task import TaskDAO


class TaskCreateCommand:
    def __init__(self, file: UploadFile):
        self._file = file

    async def run(self) -> str:
        await self.validate()
        return await TaskDAO.create_task(self._file)

    async def validate(self):
        pass
