import csv
import io
import random
from openpyxl import load_workbook
import tempfile
import shutil
import xlrd

from app.config import settings
from app.utils.minio import get_file


class FileAnalyzer:

    def __init__(self, object_name, file_type):
        self._object_name = object_name
        self._file_type = file_type

    async def __call__(self, *args, **kwargs):
        return await getattr(self, f"_handle_{self._file_type}")()

    async def _handle_csv(self):
        obj = await get_file(self._object_name)

        reader = csv.reader(
            io.TextIOWrapper(
                obj,
                encoding="utf-8"
            )
        )
        headers = next(reader)

        samples = []
        total_rows = 0

        for row in reader:
            if len(samples) < settings.FILE_SAMPLE_MAX_SIZE:
                samples.append(row)
            else:
                # 水塘抽样
                index = random.randint(
                    0,
                    total_rows
                )
                if index < settings.FILE_SAMPLE_MAX_SIZE:
                    samples[index] = row

            total_rows += 1

        return {
            "rows": total_rows,
            "columns": len(headers),
            "headers": headers,
            "samples": samples
        }

    async def _handle_xlsx(self):
        obj = await get_file(self._object_name)

        with tempfile.NamedTemporaryFile(suffix=".xlsx") as tmp:
            shutil.copyfileobj(
                obj,
                tmp
            )

            tmp.flush()

            wb = load_workbook(tmp.name, read_only=True, data_only=True)
            ws = wb.active
            rows = ws.iter_rows()
            headers = [
                c.value
                for c in next(rows)
            ]

            samples = []
            total_rows = 0

            for row in rows:
                values = [
                    c.value
                    for c in row
                ]

                if len(samples) < settings.FILE_SAMPLE_MAX_SIZE:
                    samples.append(values)
                else:
                    index = random.randint(
                        0,
                        total_rows
                    )
                    if index < settings.FILE_SAMPLE_MAX_SIZE:
                        samples[index] = values

                total_rows += 1

            wb.close()

        return {
            "rows": total_rows,
            "columns": len(headers),
            "headers": headers,
            "samples": samples
        }

    async def _handle_xls(self):
        obj = await get_file(self._object_name)

        try:
            result = {}
            with tempfile.NamedTemporaryFile(suffix=".xls") as tmp:
                shutil.copyfileobj(obj, tmp)
                tmp.flush()
                workbook = xlrd.open_workbook(tmp.name, on_demand=True)

                try:
                    sheet = workbook.sheet_by_index(0)
                    samples = []
                    for index in range(1, sheet.nrows):
                        row = sheet.row_values(index)
                        if len(samples) < settings.FILE_SAMPLE_MAX_SIZE:
                            samples.append(row)
                        else:
                            random_index = random.randint(0, index - 1)
                            if random_index < settings.FILE_SAMPLE_MAX_SIZE:
                                samples[random_index] = row

                    result = {
                        "rows": sheet.nrows - 1,
                        "columns": sheet.ncols,
                        "headers": sheet.row_values(0),
                        "samples": samples
                    }

                finally:
                    workbook.release_resources()

            return result

        finally:
            obj.close()
            obj.release_conn()
