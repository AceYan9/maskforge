import logging

from fastapi import APIRouter, UploadFile, Depends

from app.api.deps.task import validate_excel_file
from app.api.schema.common import ApiResponse
from app.commands.task import TaskCreateCommand

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("", response_model=ApiResponse, summary="Upload file")
async def upload_file(file: UploadFile = Depends(validate_excel_file)):
    command = TaskCreateCommand(file)
    task_id = await command.run()
    return {"data": {"task_id": task_id}}


@router.get("", response_model=ApiResponse, summary="Upload file")
async def test_func():
    return {"data": None}
