import logging
import pandas as pd
from pathlib import Path

from fastapi import UploadFile

from app.utils.common import generate_task_id
from app.utils.save_file import save_upload_file

logger = logging.getLogger(__name__)


class TaskDAO:

    @classmethod
    async def create_task(cls, file: UploadFile) -> str:
        task_id = await generate_task_id()
        df = await cls.read_file(file)
        await save_upload_file(task_id, file)

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
