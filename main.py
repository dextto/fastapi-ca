import uvicorn

from fastapi import FastAPI

from user.application.user_service import UserService

app = FastAPI()


@app.get("/")
def hello():
    UserService().create_user('name', 'email', 'password')
    return {"Hello": "FastAPI"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True)
