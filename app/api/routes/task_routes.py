import logging

from fastapi import APIRouter, UploadFile, Depends, Query

from app.api.deps.task import validate_excel_file, get_task_obj
from app.api.schema.common import ApiResponse
from app.api.schema.task import PreviewMaskSchema
from app.commands.task import (
    TaskCreateCommand, TaskDetailCommand, TaskPreviewCommand, TaskRunCommand, TaskRunListCommand, TaskListCommand
)
from app.models import Task

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/", response_model=ApiResponse, summary="Upload file")
async def upload_file(file: UploadFile = Depends(validate_excel_file)):
    command = TaskCreateCommand(file)
    task_id = await command.run()
    return {"data": {"task_id": task_id}}


@router.get("/", response_model=ApiResponse, summary="Get task list")
async def task_list(page: int = Query(1, ge=1), page_size: int = Query(10, ge=1, le=100)):
    command = TaskListCommand(page, page_size)
    data = await command.run()
    return {"data": data}


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


@router.post("/{task_id}/run/", response_model=ApiResponse, summary="Run mask result")
async def preview_mask(body_data: PreviewMaskSchema, task: Task = Depends(get_task_obj)):
    command = TaskRunCommand(task, body_data.rules)
    run_id = await command.run()
    return {"data": {"run_id": run_id}}


@router.get("/{task_id}/run_list/", response_model=ApiResponse, summary="Get task run list")
async def preview_mask(page: int = Query(1, ge=1), page_size: int = Query(10, ge=1, le=100), task: Task = Depends(get_task_obj)):
    command = TaskRunListCommand(task.task_id, page, page_size)
    data = await command.run()
    return {"data": data}
