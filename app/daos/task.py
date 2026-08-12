import json
import uuid
import logging

from fastapi import UploadFile

from app.models import Task, MaskRule
from app.utils.common import get_file_size
from app.utils.minio import upload_files, get_file
from app.utils.async_tasks import process_file

logger = logging.getLogger(__name__)


class TaskDAO:

    @staticmethod
    async def get_task_by_task_id(task_id: str) -> Task:
        return await Task.get_or_none(task_id=task_id)

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
    async def get_task_detail(task: Task):
        data = {
            "status": task.status,
            "filename": task.filename,
            "rows": task.total_rows,
        }
        with get_file(f"{task.task_id}/analysis/sample.json") as obj:
            data["sample_data"] = json.loads(obj.read().decode("utf-8"))
        with get_file(f"{task.task_id}/analysis/header.json") as obj:
            headers = json.loads(obj.read().decode("utf-8"))
            data["columns"] = headers

        recommended_rule = None
        if mask_rule := await MaskRule.get_or_none(task_id=task.task_id):
            recommended_rule = mask_rule.rules
        else:
            with get_file(f"{task.task_id}/analysis/recommended_rule.json") as obj:
                recommended_rule = json.loads(obj.read().decode("utf-8"))

        data["recommended_rule"] = {header: recommended_rule.get(header) or {} for header in headers}

        return data
