from pydantic import BaseModel
from typing import Optional


class TaskBase(BaseModel):
    detail: str
    is_complete: bool = False

class ShowTask(TaskBase):
    id: int
    class Config:
        orm_mode = True


class Task(TaskBase):
    id: int
    job_id: int

    class Config():
        orm_mode = True
    

class CreateTask(TaskBase):
    class Config():
        schema_extra = {
            "example": {
                "detail": "remove old floors",
                "is_complete": "false"
            }
        }


class UpdateTask(TaskBase):
    pass