from typing import Any

from app.utils.rules.base import MaskRule
from app.utils.rule_registry import register


@register("all_mask")
class AllMaskRule(MaskRule):

    def apply(self, value: str, config: dict[str, Any]):

        if value is None:
            return value

        char = config.get("mask_char", "*")

        mask_count = min(3, len(value))

        return char * mask_count

