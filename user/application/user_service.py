from datetime import datetime
from user.domain.user import User
from user.domain.repository.user_repo import IUserRepository
from user.infra.database.user_repo import UserRepository


class UserService:
    def __init__(self):
        self.user_repo: IUserRepository = UserRepository()

    def create_user(self, name: str, email: str, password: str):
        now = datetime.now()
        user: User = User(name, email, password, now, now)
        self.user_repo.save(user)

        return user
