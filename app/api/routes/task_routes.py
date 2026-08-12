import logging

from fastapi import APIRouter, UploadFile, Depends

from app.api.deps.task import validate_excel_file, get_task
from app.api.schema.common import ApiResponse
from app.commands.task import TaskCreateCommand, TaskDetailCommand

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("", response_model=ApiResponse, summary="Upload file")
async def upload_file(file: UploadFile = Depends(validate_excel_file)):
    command = TaskCreateCommand(file)
    task_id = await command.run()
    return {"data": {"task_id": task_id}}


@router.get("/{task_id}", response_model=ApiResponse, summary="Get task detail")
async def get_task(task = Depends(get_task)):
    command = TaskDetailCommand(task)
    data = await command.run()
    return {"data": data}
