from fastapi import APIRouter
from pydantic import BaseModel

from user.application.user_service import UserService

router = APIRouter(prefix="/users")


class User(BaseModel):
    name: str
    email: str
    password: str


@router.post("")
def create_user(user: User):
    user_service = UserService()
    created_user = user_service.create_user(
        name=user.name,
        email=user.email,
        password=user.password
    )

    return created_user
