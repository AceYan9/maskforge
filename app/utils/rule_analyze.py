from app.config import settings
from app.utils.recognizer.engine import RecognizerEngine
from app.utils.recognizer.plugins.phone import PhoneRecognizer
from app.utils.recognizer.plugins.email import EmailRecognizer
from app.utils.recognizer.plugins.id_card import IDCardRecognizer
from app.utils.recognizer.plugins.date import DateRecognizer, TimeRecognizer


recognizers = [
    PhoneRecognizer,
    EmailRecognizer,
    IDCardRecognizer,
    DateRecognizer,
    TimeRecognizer,
]
engine = RecognizerEngine()
for recognizer_cls in recognizers:
    engine.register(recognizer_cls())


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
        if recognize_data.get("confidence") < settings.RECOGNIZE_CONFIDENCE_THRESHOLD:
            return {}

        func = getattr(self, f"_get_{recognize_type}_rule_config")
        return await func(recognize_data)

    @staticmethod
    async def _get_phone_rule_config(data: dict = None):
        return {
            "rule_type": "middle_mask",
            "left_save_count": 3,
            "right_save_count": 4,
            "mask_char": "*",
        }

    @staticmethod
    async def _get_email_rule_config(data: dict = None):
        return {
            "rule_type": "left_mask",
            "anchor": "@",
            "anchor_side": "left",
            "count": 4,
            "mask_char": "*",
        }

    @staticmethod
    async def _get_id_card_rule_config(data: dict = None):
        return {
            "rule_type": "middle_mask",
            "left_save_count": 4,
            "right_save_count": 3,
            "mask_char": "*",
        }

    @staticmethod
    async def _get_date_rule_config(data: dict = None):
        return {
            "rule_type": "date_offset_mask",
            "format": data.get("format"),
            "date_offset": {
                "min": -12,
                "max": 12,
            }
        }

    @staticmethod
    async def _get_time_rule_config(data: dict = None):
        return {
            "rule_type": "time_offset_mask",
            "format": data.get("format"),
            "time_offset": {
                "min": "-02:00:00",
                "max": "02:00:00",
            }
        }
