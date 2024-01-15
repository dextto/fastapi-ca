from typing import Annotated
from fastapi import APIRouter, Depends
from config import Settings, get_settings

router = APIRouter(prefix="/env-test")


@router.get("")
async def info(settings: Annotated[Settings, Depends(get_settings)]):
    return {
        "database_username": settings.database_username,
        "database_password": settings.database_password,
        "jwt_secret": settings.jwt_secret,
    }
