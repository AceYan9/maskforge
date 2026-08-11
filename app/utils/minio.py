import io
import json
from typing import Any
from contextlib import contextmanager

from minio import Minio
from fastapi import UploadFile, File

from app.config import settings


client = Minio(
    endpoint=settings.MINIO_ENDPOINT,
    access_key=settings.MINIO_ACCESS_KEY,
    secret_key=settings.MINIO_SECRET_KEY,
    secure=False
)


def init_bucket():
    """
    初始化 bucket
    """
    if not client.bucket_exists(settings.MINIO_BUCKET):
        client.make_bucket(settings.MINIO_BUCKET)


async def upload_files(task_id: str, files: list[UploadFile] = File(...)):
    result = []
    for file in files:
        object_name = f"{task_id}/source/{file.filename}"
        client.put_object(
            settings.MINIO_BUCKET,
            object_name,
            file.file,
            -1,
            part_size=10 * 1024 * 1024,
        )
        result.append(object_name)

    return result


@contextmanager
def get_file(object_name: str):
    obj = client.get_object(
        settings.MINIO_BUCKET,
        object_name,
    )
    try:
        yield obj
    finally:
        obj.close()
        obj.release_conn()


async def submit_analysis_data(task_id: str, data: list | dict, filename: str):
    object_name = f"{task_id}/analysis/{filename}"
    content = json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8")

    client.put_object(
        settings.MINIO_BUCKET,
        object_name,
        io.BytesIO(content),
        length=len(content),
        content_type="application/json",
    )
    return object_name
