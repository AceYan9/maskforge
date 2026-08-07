import shutil
from fastapi import UploadFile
from app.config import settings


async def save_upload_file(task_id: str, file: UploadFile):
    dir_path = settings.TASK_DIR / task_id / "source"
    dir_path.mkdir(parents=True, exist_ok=True)
    file_path = dir_path / file.filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return file_path
