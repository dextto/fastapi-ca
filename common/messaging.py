from celery import Celery

from config import get_settings
from user.application.send_welcome_email_task import SendWelcomeEmailTask

settings = get_settings()

celery = Celery(
    "fastapi-ca",
    broker=settings.celery_broker_url,
    backend=settings.celery_backend_url,
    broker_connection_retry_on_startup=True,
    include=["example.ch10_02.celery_task"],
)

celery.register_task(SendWelcomeEmailTask())
