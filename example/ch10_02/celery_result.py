from celery.result import AsyncResult

from common.messaging import celery


if __name__ == "__main__":
    async_result = AsyncResult("eb8a6377-34a8-4e17-9805-491098ae4962", app=celery)
    result = async_result.result

    print(result)
