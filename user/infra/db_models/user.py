from sqlalchemy import Column, String, DateTime

from database import Base


class User(Base):
    __tablename__ = "User"

    id = Column(String(36), primary_key=True)
    email = Column(String(64), nullable=False)
    password = Column(String(64), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
