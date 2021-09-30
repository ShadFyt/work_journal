from pydantic import BaseModel
from typing import Optional


class TaskBase(BaseModel):
    detail: str
    is_complete: bool = False
    


class Task(TaskBase):
    id: int

    class Config():
        orm_mode = True
    

class CreateTask():

    class Config():
        schema_extra = {
            "example": {
                "detail": "remove old floors",
                "is_complete": "false"
            }
        }