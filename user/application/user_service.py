from fastapi import HTTPException
from ulid import ULID
from datetime import datetime
from user.domain.user import User
from user.domain.repository.user_repo import IUserRepository
from user.infra.database.user_repo import UserRepository
from utils.crypto import Crypto


class UserService:
    def __init__(self):
        self.user_repo: IUserRepository = UserRepository()
        self.crypto = Crypto()
        self.ulid = ULID()

    def create_user(self, name: str, email: str, password: str):
        try:
            self.user_repo.find_by_email(email)
        except HTTPException as e:
            if e.status_code != 422:
                raise e

        now = datetime.now()
        user: User = User(
            id=self.ulid.generate(),
            name=name,
            email=email,
            password=self.crypto.encrypt(password),
            created_at=now,
            updated_at=now,
        )
        self.user_repo.save(user)

        return user
