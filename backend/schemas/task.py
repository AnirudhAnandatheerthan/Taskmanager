from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional, List

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: datetime

class TaskCreate(TaskBase):
    user_id: int

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[datetime] = None

class TaskResponse(TaskBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
