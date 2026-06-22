from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession
from backend.services.task_service import create_task, get_tasks, get_task, update_task, delete_task
from backend.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from backend.db.session import get_session

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_new_task(task: TaskCreate, db: AsyncSession = Depends(get_session)):
    return await create_task(db, task)

@router.get("/", response_model=List[TaskResponse])
async def read_tasks(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_session)):
    return await get_tasks(db, skip, limit)

@router.get("/{task_id}", response_model=TaskResponse)
async def read_task(task_id: int, db: AsyncSession = Depends(get_session)):
    task = await get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=TaskResponse)
async def update_existing_task(task_id: int, task_update: TaskUpdate, db: AsyncSession = Depends(get_session)):
    updated_task = await update_task(db, task_id, task_update)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task_item(task_id: int, db: AsyncSession = Depends(get_session)):
    success = await delete_task(db, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
