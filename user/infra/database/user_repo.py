from user.domain.repository.user_repo import IUserRepository
from user.domain.user import User


class UserRepository(IUserRepository):
    def save(self, user: User):
        pass

    def find_by_email(self, email: str) -> User:
        pass
