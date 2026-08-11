from datetime import datetime

from ..base import BaseRecognizer



class DateRecognizer(BaseRecognizer):

    name = "date"
    formats = [
        "%Y-%m-%d",
        "%Y/%m/%d",
        "%Y.%m.%d",
        "%Y%m%d",
        "%Y-%m-%d %H:%M:%S",
        "%Y/%m/%d %H:%M:%S",
        "%Y-%m-%d %H:%M",
        "%Y/%m/%d %H:%M",
    ]

    def parse(self,value):
        for fmt in self.formats:
            try:
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
