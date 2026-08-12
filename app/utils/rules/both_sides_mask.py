from typing import Any

from app.utils.rules.base import MaskRule
from app.utils.rule_registry import register


@register("both_sides_mask")
class BothSidesMaskRule(MaskRule):

    def apply(self, value: str, config: dict[str, Any]):

        if value is None:
            return value

        length = len(value)
        left_count = config.get("left_count", 1)
        right_count = config.get("right_count", 1)
        char = config.get("mask_char", "*")

        if left_count + right_count >= length:
            return char * length

        return char * left_count + value[left_count: (length - right_count)] + char * right_count
