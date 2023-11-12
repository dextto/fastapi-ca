from fastapi import HTTPException
from database import SessionLocal
from user.domain.repository.user_repo import IUserRepository
from user.domain.user import User as UserVO
from user.infra.db_models.user import User


class UserRepository(IUserRepository):
    def save(self, user: UserVO):
        new_user = User(
            id=user.id,
            name=user.name,
            email=user.email,
            password=user.password,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

        with SessionLocal() as session:
            session = SessionLocal()
            session.add(new_user)
            session.commit()

    def find_by_email(self, email: str) -> UserVO:
        with SessionLocal() as session:
            user = session.query(User).filter(User.email == email).first()

        if not user:
            raise HTTPException(status_code=422)

        return UserVO(
            id=user.id,
            name=user.name,
            email=user.email,
            password=user.password,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )
