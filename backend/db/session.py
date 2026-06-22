from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from backend.core.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=False)

async def get_session():
    async with AsyncSession(engine) as session:
        yield session
