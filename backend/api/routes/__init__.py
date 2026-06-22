from fastapi import APIRouter
from . import users, tasks, health

router = APIRouter()
router.include_router(users.router)
router.include_router(tasks.router)
router.include_router(health.router)
