from containers import Container
import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from user.interface.controllers.user_controller import router as user_routers


app = FastAPI()
app.container = Container()

app.include_router(user_routers)


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
