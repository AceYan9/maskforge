from typing import Any

from app.utils.rules.base import MaskRule
from app.utils.rule_registry import register


@register("right_mask")
class RightMaskRule(MaskRule):

    def apply(self, value: str, config: dict[str, Any]):

        if value is None:
            return value

        anchor_side = config.get("anchor_side", "left")
        anchor = config.get("anchor") or ""
        mask_value, unchange_value = self._handle_value_with_anchor(value, anchor, anchor_side)

        count = config.get("count", 1)
        char = config.get("mask_char", "*")

        mask_count = min(count, len(mask_value))
        masked_value = mask_value[:mask_count] + char * mask_count
        if not unchange_value:
            return masked_value
        return (masked_value + anchor + unchange_value) if anchor_side == "left" else (unchange_value + anchor + masked_value)
