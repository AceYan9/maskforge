import re

from app.utils.recognizer.base import BaseRecognizer


class PhoneRecognizer(BaseRecognizer):

    name = "phone"
    pattern = re.compile(r"^1[3-9]\d{9}$")

    def recognize(self, column_name, values):
        matched = sum(bool(self.pattern.match(v)) for v in values)

        return {
            "type": self.name,
            "confidence": matched / len(values),
            "matched": matched
        }