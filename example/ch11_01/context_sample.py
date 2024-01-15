import asyncio
from contextvars import ContextVar
from fastapi import APIRouter

foo_context: ContextVar[str] = ContextVar("foo", default="bar")

router = APIRouter(prefix="/context")


@router.get("")
async def context_test(var: str):
    foo_context.set(var)
    await asyncio.sleep(1)

    return {
        "var": var,
        "context_var": foo_context.get(),
    }
