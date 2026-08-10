import uuid

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
        object_name = f"{task_id}/{uuid.uuid4()}-{file.filename}"
        client.put_object(
            settings.MINIO_BUCKET,
            object_name,
            file.file,
            -1,
            part_size=10 * 1024 * 1024,
        )
        result.append(object_name)

    return result


async def get_file(object_name: str):
    return client.get_object(
        settings.MINIO_BUCKET,
        object_name,
    )
