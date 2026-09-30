import re
import random

from fastapi import UploadFile

from app.utils.const import FORMAT_MAP

FORMAT_PATTERN = re.compile(
    r"YYYY|MM|DD|HH|mm|ss"
)


async def get_file_size(file: UploadFile) -> int:
    file.file.seek(0, 2)  # 移动到文件末尾
    size = file.file.tell()  # 获取当前位置，也就是大小
    file.file.seek(0)  # 重置指针

    return size


def to_python_format(format_str: str) -> str:
    return FORMAT_PATTERN.sub(
        lambda m: FORMAT_MAP[m.group()],
        format_str,
    )


def to_seconds(value: str) -> int:
    sign = -1 if value.startswith("-") else 1
    value = value.lstrip("-")

    h, m, s = map(int, value.split(":"))
    return sign * (h * 3600 + m * 60 + s)


def random_second(start: str, end: str) -> int:
    start_seconds = to_seconds(start)
    end_seconds = to_seconds(end)

    seconds = random.randint(start_seconds, end_seconds)

    return seconds
