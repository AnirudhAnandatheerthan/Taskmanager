from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from fastapi import HTTPException
from backend.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from backend.db.models import Task, User

async def create_task(db: AsyncSession, task_data: TaskCreate) -> TaskResponse:
    stmt = select(User).where(User.id == task_data.user_id)
    users = await db.exec(stmt)
    existing_user = users.first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    stmt = select(Task).where(Task.title == task_data.title)
    tasks = await db.exec(stmt)
    existing_task = tasks.first()
    if existing_task:
        raise HTTPException(status_code=400, detail="Task already exists")

    db_task = Task(**task_data.model_dump())
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return TaskResponse.model_validate(db_task)

async def get_tasks(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[TaskResponse]:
    stmt = select(Task).offset(skip).limit(limit)
    tasks = await db.exec(stmt)
    return [TaskResponse.model_validate(t) for t in tasks.all()]

async def get_task(db: AsyncSession, task_id: int) -> TaskResponse | None:
    task = await db.get(Task, task_id)
    if not task:
        return None
    return TaskResponse.model_validate(task)

async def update_task(db: AsyncSession, task_id: int, task_update: TaskUpdate) -> TaskResponse | None:
    task = await db.get(Task, task_id)
    if not task:
        return None
    
    update_data = task_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(task, key, value)
        
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return TaskResponse.model_validate(task)

async def delete_task(db: AsyncSession, task_id: int) -> bool:
    task = await db.get(Task, task_id)
    if not task:
        return False
    await db.delete(task)
    await db.commit()
    return True
