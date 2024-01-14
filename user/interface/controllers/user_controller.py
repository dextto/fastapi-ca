from typing import Annotated
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from containers import Container

from user.application.user_service import UserService

router = APIRouter(prefix="/users")


class User(BaseModel):
    name: str
    email: str
    password: str


@router.post("", status_code=201)
@inject
def create_user(
    user: User,
    # user_service: Annotated[UserService, Depends(UserService)],
    user_service: UserService = Depends(Provide[Container.user_service]),
    # user_service: UserService = Depends(Provide["user_service"]),  # 리터럴 문자열을 이용할 경우
):
    created_user = user_service.create_user(
        name=user.name, email=user.email, password=user.password
    )

    return created_user
