from fastapi import UploadFile


async def get_file_size(file: UploadFile) -> int:
    file.file.seek(0, 2)  # 移动到文件末尾
    size = file.file.tell()  # 获取当前位置，也就是大小
    file.file.seek(0)  # 重置指针

    return size
