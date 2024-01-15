from datetime import datetime
import time

from fastapi import APIRouter

router = APIRouter(prefix="/sync-test")


def sync_task(num):
    print("sync_task: ", num)
    time.sleep(1)
    return num


@router.get("")
def sync_example():
    now = datetime.now()
    results = [sync_task(1), sync_task(2), sync_task(3)]
    print(datetime.now() - now)

    return {"results": results}
