import logging

from app.utils.rule_registry import get_rule

logger = logging.getLogger(__name__)


class MaskEngine:

    def apply_dataframe(self, df, rules):
        result = df.copy()

        for column, rule in rules.items():
            if column not in result.columns:
                continue

            logger.info(f"{column=} {result[column]=} {rule=}")
            result[column] = result[column].apply(lambda x: self.apply_value(x, rule))

        return result

    @staticmethod
    def apply_value(value, rule):
        if not rule:
            return value

        rule_type = rule["rule_type"]
        handler = get_rule(rule_type)

        if not handler:
            raise ValueError(f"Unknown rule type: {rule_type}")

        return handler.apply(value, rule.get("config", {}))
