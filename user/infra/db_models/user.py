from sqlalchemy import Column, String, DateTime

from database import Base


class User(Base):
    __tablename__ = "User"

    id = Column(String(36), primary_key=True)
    name = Column(String(32), nullable=False)
    email = Column(String(64), nullable=False)
    password = Column(String(64), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
