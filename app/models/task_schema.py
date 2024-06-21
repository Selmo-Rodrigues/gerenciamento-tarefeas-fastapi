from pydantic import BaseModel, ConfigDict
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: str

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    status: str

class Task(TaskBase):
    id: int
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
