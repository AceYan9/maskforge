import re
from datetime import datetime

from app.utils.recognizer.base import BaseRecognizer


class IDCardRecognizer(BaseRecognizer):

    name = "id_card"


    pattern = re.compile(r"^\d{17}[\dXx]$")


    def recognize(self, column_name, values):
        matched = 0

        for value in values:
            if not self.pattern.match(value):
                continue

            birthday = value[6:14]
            try:
                datetime.strptime(birthday, "%Y%m%d")
                matched += 1
            except ValueError:
                pass

        return {
            "type": self.name,
            "confidence": matched / len(values),
            "matched": matched
        }
