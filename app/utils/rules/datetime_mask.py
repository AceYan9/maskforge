from datetime import datetime, timedelta

from app.utils.rules.base import MaskRule
from app.utils.rule_registry import register
from app.utils.common import to_python_format


def _handle_date_or_time_mask(value, config):
    def _mask_indexes(indexes):
        chars = list(value)

        for index in indexes:
            chars[index] = char

        return "".join(chars)

    if value is None:
        return value

    if not (fmt := config.get("format")):
        return value

    if not (hides := config.get("hides")) or not isinstance(hides, list):
        return value

    char = config.get("mask_char", "*")
    run_fmt = to_python_format(fmt)
    hide_indexes = []
    try:
        datetime.strptime(value, run_fmt)
    except Exception:
        return value
    else:
        for hide_fmt in hides:
            try:
                idx = fmt.index(hide_fmt)
            except:
                pass
            else:
                hide_indexes += [idx + i for i in range(len(hide_fmt))]

    if not hide_indexes:
        return value

    return _mask_indexes(hide_indexes)


@register("date_mask")
class DateMaskRule(MaskRule):

    def apply(self, value, config):
        return _handle_date_or_time_mask(value, config)


@register("date_offset_mask")
class DateOffsetMaskRule(MaskRule):

    def apply(self, value, config):

        if value is None:
            return value

        if not (day_offset := config.get("date_offset_val")):
            return value

        if not (fmt := config.get("format")):
            return value

        fmt = to_python_format(fmt)
        try:
            dt = datetime.strptime(value, fmt)
            dt += timedelta(days=day_offset)
            return datetime.strftime(dt, fmt)
        except Exception:
            return value


@register("time_mask")
class TimeMaskRule(MaskRule):

    def apply(self, value, config):
        return _handle_date_or_time_mask(value, config)


@register("time_offset_mask")
class TimeOffsetMaskRule(MaskRule):

    def apply(self, value, config):

        if value is None:
            return value

        if not (second_offset := config.get("time_offset_val")):
            return value

        if not (fmt := config.get("format")):
            return value

        fmt = to_python_format(fmt)
        try:
            dt = datetime.strptime(value, fmt)
            dt += timedelta(seconds=second_offset)
            return datetime.strftime(dt, fmt)
        except Exception:
            return value
