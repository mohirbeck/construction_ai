from pydantic import BaseModel
from typing import List
from datetime import datetime
from enum import Enum as PyEnum

class ProjectStatus(str, PyEnum):
    processing = "processing"
    in_progress = "in_progress"
    completed = "completed"

class TaskStatus(str, PyEnum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"

class TaskBase(BaseModel):
    name: str
    status: TaskStatus

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int

    class Config:
        from_attributes = True

class ProjectBase(BaseModel):
    project_name: str
    location: str

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    status: ProjectStatus
    created_at: datetime
    tasks: List[Task] = []

    class Config:
        from_attributes = True