from pathlib import Path

from fastapi import UploadFile, HTTPException, status


ALLOWED_FILE_TYPES = {
    ".csv": {
        "text/csv",
        "application/csv",
        "application/vnd.ms-excel",
    },
    ".xls": {
        "application/vnd.ms-excel",
    },
    ".xlsx": {
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    },
}


async def validate_excel_file(file: UploadFile) -> UploadFile:
    """
    校验上传文件类型：
    1. 文件后缀
    2. MIME Type
    """

    if not file.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="文件名不能为空"
        )

    suffix = Path(file.filename).suffix.lower()

    # 校验后缀
    if suffix not in ALLOWED_FILE_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="仅支持 CSV、XLS、XLSX 文件"
        )

    # 校验 MIME Type
    if file.content_type not in ALLOWED_FILE_TYPES[suffix]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"文件类型错误，不支持 {file.content_type}"
        )

    return file
