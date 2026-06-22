from fastapi import APIRouter, Depends, status
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import text
from backend.db.session import get_session

router = APIRouter(prefix="/health", tags=["health"])

@router.get("/", status_code=status.HTTP_200_OK)
async def health_check(db: AsyncSession = Depends(get_session)):
    try:
        await db.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": "disconnected", "error": str(e)}
