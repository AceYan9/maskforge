from typing import Any

from app.utils.rules.base import MaskRule
from app.utils.rule_registry import register


@register("right_mask")
class RightMaskRule(MaskRule):

    def apply(self, value: str, config: dict[str, Any]):

        if value is None:
            return value

        length = len(value)
        count = config.get("count", 1)
        char = config.get("mask_char", "*")

        return value[:(length - count)] + char * count
