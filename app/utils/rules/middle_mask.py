from typing import Any

from app.utils.rules.base import MaskRule
from app.utils.rule_registry import register


@register("middle_mask")
class MiddleMaskRule(MaskRule):

    def apply(self, value: str, config: dict[str, Any]):

        if value is None:
            return value

        length = len(value)
        left_save_count = config.get("left_save_count", 1)
        right_save_count = config.get("right_save_count", 1)
        count = length - left_save_count - right_save_count
        char = config.get("mask_char", "*")

        return value[:left_save_count] + char * count + value[left_save_count + count:]
