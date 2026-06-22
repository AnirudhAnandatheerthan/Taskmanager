from fastapi import APIRouter, Depends, status
from sqlmodel.ext.asyncio.session import AsyncSession
from backend.services.user_service import create_user
from backend.schemas.user import UserCreate, UserResponse
from backend.db.session import get_session

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_session)):
    return await create_user(db, user)
