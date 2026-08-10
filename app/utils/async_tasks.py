import asyncio

from app.celery_app import celery_app, BaseTask
from app.models import Task


class ProcessFileTask(BaseTask):

    async def run_async(self, task_id):

        await self.init_db()

        task = await Task.get_or_none(
            task_id=task_id
        )

        if not task:
            return

        # todo get the number of rows, columns, and sample data of up to 100 rows
        print("processing")


process_file = celery_app.register_task(ProcessFileTask())
