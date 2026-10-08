import hashlib

from app.config import settings
from app.utils.rules.base import MaskRule
from app.utils.rule_registry import register


@register("hash_mask")
class HashMaskRule(MaskRule):

    def apply(self, value, config):

        if value is None:
            return value

        raw = str(value) + settings.MASK_HASH_SALT
        algorithm = config.get("algorithm", "sha256")

        hash_func = getattr(hashlib, algorithm)

        return hash_func(raw.encode()).hexdigest()
