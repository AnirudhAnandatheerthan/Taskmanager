from http.client import HTTPResponse

from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from fastapi import HTTPException
from backend.schemas.user import UserCreate, UserResponse
from backend.db.models import User

async def create_user(db: AsyncSession, user_data: UserCreate) -> UserResponse:
    stmt = select(User).where(User.email == user_data.email)

    existing_user = await db.exec(stmt)
    first_user = existing_user.first()
    print(first_user, type(first_user))
    if first_user is not None:
        raise HTTPException(status_code=400, detail="Email already registered")

    db_user = User(email=user_data.email, password=user_data.password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return UserResponse.model_validate(db_user)
