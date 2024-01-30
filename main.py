from containers import Container
import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from user.interface.controllers.user_controller import router as user_routers
from note.interface.controllers.note_controller import router as note_routers
from example.ch06_02.sync_ex import router as sync_ex_routers
from example.ch06_02.async_ex import router as async_ex_routers
from example.ch08_03.env_ex import router as env_ex_routers
from example.ch11_01.middleware import create_sample_middleware
from example.ch11_01.context_sample import router as context_ex_router


app = FastAPI()
app.container = Container()

app.include_router(user_routers)
app.include_router(note_routers)

app.include_router(sync_ex_routers)
app.include_router(async_ex_routers)
app.include_router(env_ex_routers)
app.include_router(context_ex_router)

create_sample_middleware(app)  # 미들웨어를 등록한다


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content=str(exc.errors()),
    )


@app.get("/")
def hello():
    return {"Hello": "FastAPI"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True)
