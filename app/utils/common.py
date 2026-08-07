import uuid
from app.config import settings


async def generate_task_id() -> str:
    while 1:
        task_id = uuid.uuid4().hex
        task_dir = settings.TASK_DIR / task_id
        if not task_dir.exists():
            return task_id
