from datetime import datetime
from user.domain.user import User
from user.domain.repository.user_repo import IUserRepository
from user.infra.database.user_repo import UserRepository
from utils.crypto import Crypto


class UserService:
    def __init__(self):
        self.user_repo: IUserRepository = UserRepository()
        self.crypto = Crypto()

    def create_user(self, name: str, email: str, password: str):
        self.user_repo.find_by_email(email)

        encrypted_password = self.crypto.encrypt(password)

        now = datetime.now()
        user: User = User(name, email, encrypted_password, now, now)
        self.user_repo.save(user)

        return user
