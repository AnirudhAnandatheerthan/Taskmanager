from fastapi import FastAPI
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from .core.config import settings
from .api.routes import router as api_router

app = FastAPI(
    title=settings.APP_NAME,
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(api_router, prefix="/api/v1")

@app.on_event("startup")
async def create_tables():
    engine = create_async_engine(settings.DATABASE_URL)
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    await engine.dispose()

@app.get("/")
async def root():
    return {"message": "Welcome to the Task Manager API"}
