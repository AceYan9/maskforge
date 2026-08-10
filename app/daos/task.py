import uuid
import logging
import pandas as pd
from pathlib import Path

from fastapi import UploadFile

from app.models import Task
from app.utils.common import get_file_size
from app.utils.minio import upload_files
from app.utils.async_tasks import process_file

logger = logging.getLogger(__name__)


class TaskDAO:

    @staticmethod
    async def generate_task_id():
        while 1:
            task_id = uuid.uuid4().hex
            if not await Task.get_or_none(task_id=task_id):
                return task_id

    @classmethod
    async def create_task(cls, file: UploadFile) -> str:
        task_id = await cls.generate_task_id()
        file_size = await get_file_size(file)
        source_objects = await upload_files(task_id, [file])

        await Task.create(
            task_id=task_id,
            filename=file.filename,
            file_type=file.filename.rsplit(".")[-1],
            file_size=file_size,
            source_object=source_objects[0],
        )
        process_file.delay(task_id)

        return task_id

    @staticmethod
    async def read_file(file: UploadFile) -> pd.DataFrame:
        suffix = Path(file.filename).suffix.lower()

        if suffix == ".csv":
            return pd.read_csv(file.file)

        elif suffix == ".xls":
            return pd.read_excel(file.file, engine="xlrd")

        elif suffix == ".xlsx":
            return pd.read_excel(file.file, engine="openpyxl")

        else:
            raise ValueError(f"不支持的文件类型: {suffix}")
