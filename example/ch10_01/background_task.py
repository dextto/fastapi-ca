import asyncio

from fastapi import APIRouter, BackgroundTasks

router = APIRouter(prefix="/bg-task-test")


async def perform_task(task_id: int):
    await asyncio.sleep(3)
    print(f"{task_id}번 태스크 수행 완료!")


@router.post("")
def create_task(task_id: int, background_tasks: BackgroundTasks):
    background_tasks.add_task(perform_task, task_id)
    return {"message": "태스크가 생성되었습니다"}
