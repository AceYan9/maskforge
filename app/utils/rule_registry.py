RULES = {}


def register(name):
    def decorator(cls):
        RULES[name] = cls()
        return cls
    return decorator


def get_rule(rule_type):
    return RULES.get(rule_type)
