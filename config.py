from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    database_username: str
    database_password: str
    jwt_secret: str
    email_password: str
    celery_broker_url: str
    celery_backend_url: str


@lru_cache
def get_settings():
    return Settings()


# get_settings.cache_clear()
