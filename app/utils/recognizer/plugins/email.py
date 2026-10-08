import re

from app.utils.recognizer.base import BaseRecognizer


class EmailRecognizer(BaseRecognizer):

    name = "email"
    pattern = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

    def recognize(self, column_name, values):
        matched = sum(bool(self.pattern.match(v)) for v in values)

        return {
            "type": self.name,
            "confidence": matched / len(values),
            "matched": matched
        }
