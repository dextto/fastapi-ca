import asyncio
from datetime import datetime
from fastapi import APIRouter

router = APIRouter(prefix="/async-test")


async def async_task(num):
    print("async_task: ", num)
    await asyncio.sleep(1)
    return num


@router.get("")
async def async_example():
    now = datetime.now()
    results = await asyncio.gather(
        async_task(1), async_task(2), async_task(3)
    )
    print(datetime.now() - now)

    return {"results": results}
