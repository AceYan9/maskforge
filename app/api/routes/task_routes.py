import logging

from fastapi import APIRouter, UploadFile, Depends

from app.api.deps.task import validate_excel_file, get_task_obj
from app.api.schema.common import ApiResponse
from app.api.schema.task import PreviewMaskSchema
from app.commands.task import TaskCreateCommand, TaskDetailCommand, TaskPreviewCommand
from app.models import Task

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/", response_model=ApiResponse, summary="Upload file")
async def upload_file(file: UploadFile = Depends(validate_excel_file)):
    command = TaskCreateCommand(file)
    task_id = await command.run()
    return {"data": {"task_id": task_id}}


@router.get("/{task_id}/", response_model=ApiResponse, summary="Get task detail")
async def get_task(task: Task = Depends(get_task_obj)):
    command = TaskDetailCommand(task)
    data = await command.run()
    return {"data": data}


@router.post("/{task_id}/preview/", response_model=ApiResponse, summary="Preview mask result")
async def preview_mask(body_data: PreviewMaskSchema, task: Task = Depends(get_task_obj)):
    command = TaskPreviewCommand(task, body_data.rules)
    data = await command.run()
    return {"data": data}
