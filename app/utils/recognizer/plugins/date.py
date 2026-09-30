from datetime import datetime

from app.utils.common import to_python_format
from app.utils.recognizer.base import BaseRecognizer
from app.utils.const import DATE_FORMATS, TIME_FORMATS, DATE_TIME_FORMATS


class DateTimeRecognizer(BaseRecognizer):

    formats = DATE_FORMATS + TIME_FORMATS + DATE_TIME_FORMATS

    def parse(self,value):
        for fmt in self.formats:
            try:
                fmt = to_python_format(fmt)
                datetime.strptime(value, fmt)
                return fmt
            except ValueError:
                pass
        return None

    def recognize(self, column_name, values):
        counter = {}
        for value in values:
            fmt = self.parse(value)
            if fmt:
                counter[fmt] = counter.get(fmt, 0) + 1

        if not counter:
            return {
                "type": self.name,
                "confidence":0
            }

        fmt, matched = max(counter.items(), key=lambda x:x[1])
        return {
            "type": self.name,
            "format":fmt,
            "confidence": matched / len(values),
            "matched":matched
        }


class DateRecognizer(DateTimeRecognizer):

    name = "date"
    formats = DATE_FORMATS + DATE_TIME_FORMATS


class TimeRecognizer(DateTimeRecognizer):

    name = "time"
    formats = TIME_FORMATS
