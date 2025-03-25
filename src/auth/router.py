from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .utils import hash_password
from models import UserModel
from .schemas import UserSchema
from database import get_session

router = APIRouter(prefix="/auth", tags=["auth 🥷"])


@router.post("/register/")
async def registration(user_schema: UserSchema, db: AsyncSession = Depends(get_session)):
    hashed_password = hash_password(user_schema.password)
    new_user = UserModel(
        username=user_schema.username, email=user_schema.email, password=hashed_password
    )

    db.add(new_user)
    await db.commit()

    return {"status": status.HTTP_200_OK}
