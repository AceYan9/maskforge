import asyncio

from celery import Celery, Task
from tortoise import Tortoise

from app.config import settings


celery_app = Celery(
    settings.PROJECT_NAME,
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_BACKEND_URL,
    include=[
        "app.utils.async_tasks",
    ],
)
celery_app.conf.update(
    task_track_started=True,
    timezone="Asia/Shanghai",
    enable_utc=True,
    result_expires=60 * 60,
)


class BaseTask(Task):

    abstract = True

    def __call__(self, *args, **kwargs):

        return asyncio.run(
            self.run_async(*args, **kwargs)
        )


    async def run_async(self, *args, **kwargs):
        raise NotImplementedError


    async def init_db(self):

        if not Tortoise._inited:
            await Tortoise.init(
                config=settings.TORTOISE_ORM
            )
