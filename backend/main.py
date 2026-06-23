from fastapi import FastAPI
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from .core.config import settings
from .api.routes import router as api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title=settings.APP_NAME,
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(api_router, prefix="/api/v1")


origins = [
    "http://localhost:8000",    # React default port
    "http://127.0.0.1:8000",
    "http://0.0.0.0:8000",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Allows specific origins
    allow_credentials=True,
    allow_methods=["*"],              # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],              # Allows all headers
)

@app.on_event("startup")
async def create_tables():
    engine = create_async_engine(settings.DATABASE_URL)
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    await engine.dispose()

@app.get("/")
async def root():
    return {"message": "Welcome to the Task Manager API"}


