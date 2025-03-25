from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .utils import hash_password, check_password
from models import UserModel
from .schemas import UserSchemaRegister, UserSchemaLogin
from database import get_session

router = APIRouter(prefix="/auth", tags=["auth 🥷"])


@router.post("/register/")
async def registration(
    user_schema: UserSchemaRegister, db: AsyncSession = Depends(get_session)
):
    hashed_password = hash_password(user_schema.password)
    new_user = UserModel(
        username=user_schema.username, email=user_schema.email, password=hashed_password
    )

    db.add(new_user)
    await db.commit()

    return {"status": status.HTTP_200_OK}


@router.post("/login/")
async def login(
    user_schema: UserSchemaLogin, db: AsyncSession = Depends(get_session)
):
    user = await db.execute(select(UserModel).where(UserModel.email == user_schema.email))
    user = user.scalar_one_or_none()

    if not user or not check_password(user_schema.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
    
    return {"id": user.id, "username": user.username, "email": user.email}