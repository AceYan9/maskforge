from app.utils.recognizer.engine import RecognizerEngine

from app.utils.recognizer.plugins.phone import PhoneRecognizer
from app.utils.recognizer.plugins.email import EmailRecognizer
from app.utils.recognizer.plugins.id_card import IDCardRecognizer
from app.utils.recognizer.plugins.date import DateRecognizer


engine = RecognizerEngine()
engine.register(PhoneRecognizer())
engine.register(EmailRecognizer())
engine.register(IDCardRecognizer())
engine.register(DateRecognizer())


class RuleAnalyzer:

    def __init__(self, sample_data: list, headers: list):
        self._sample_data = sample_data
        self._headers = headers

    async def __call__(self, *args, **kwargs):
        result = {}
        for header in self._headers:
            data = [str(item[header]) if item.get(header) else "" for item in self._sample_data]
            recognize_data = engine.recognize(header, data)
            result[header] = await self._get_recommended_rule_config(recognize_data)

        return result

    async def _get_recommended_rule_config(self, recognize_data: dict) -> dict:
        recognize_type = recognize_data.get("type")
        if recognize_data.get("confidence") < 0.95:
            return {}

        func = getattr(self, f"_get_{recognize_type}_rule_config")
        return await func()

    @staticmethod
    async def _get_phone_rule_config():
        return {
            "rule_type": "middle_mask",
            "left_save_count": 3,
            "right_save_count": 4,
            "mask_char": "*",
        }

    @staticmethod
    async def _get_email_rule_config():
        return {
            "rule_type": "left_mask",
            "anchor": "@",
            "anchor_side": "left",
            "count": 4,
            "mask_char": "*",
        }

    @staticmethod
    async def _get_id_card_rule_config():
        return {
            "rule_type": "middle_mask",
            "left_save_count": 4,
            "right_save_count": 3,
            "mask_char": "*",
        }

    @staticmethod
    async def _get_date_rule_config():
        return {}
