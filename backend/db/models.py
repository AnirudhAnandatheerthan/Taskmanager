from datetime import datetime, timedelta
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from .base import Base

class User(Base, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    password: str = Field(sa_column=Field(index=False))  # Placeholder for hashed password
    is_active: bool = True
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    updated_at: datetime = Field(default_factory=lambda: datetime.now())
    
    tasks: List["Task"] = Relationship(back_populates="user")

class Task(Base, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    due_date: datetime = Field(default_factory=lambda: datetime.now(tzinfo=None) + timedelta(days=7))  # Default due date is 7 days from now
    user_id: int = Field(foreign_key="user.id")
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    updated_at: datetime = Field(default_factory=lambda: datetime.now())
    
    user: User = Relationship(back_populates="tasks")
