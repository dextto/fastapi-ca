from contextvars import ContextVar

user_context: dict | None = ContextVar("current_user", default=None)
