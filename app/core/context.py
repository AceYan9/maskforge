from contextvars import ContextVar


current_timezone: ContextVar[str] = ContextVar(
    "current_timezone",
    default="UTC",
)
