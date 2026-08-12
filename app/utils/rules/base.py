from abc import ABC, abstractmethod


class MaskRule(ABC):

    @abstractmethod
    def apply(self, value, config):
        pass

    @staticmethod
    def _handle_value_with_anchor(value: str, anchor: str, anchor_side: str):
        mask_value, unchange_value = value, ""
        if anchor and anchor in value:
            idx = value.index(anchor)
            if anchor_side == "left":
                mask_value = value[:idx]
                unchange_value = value[idx + 1:]
            else:
                mask_value = value[idx + 1:]
                unchange_value = value[:idx]

        return mask_value, unchange_value
