from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date

from schemas import task_schema

class JobBase(BaseModel):
    name: str
    location: str
    details: Optional[str] = None
    is_complete: bool = False
    date: date

class ShowJob(JobBase):
    id: int
    class Config:
        orm_mode=True

class JobInDb(JobBase):
    id: int
    tasks: List[task_schema.Task] = []


    class Config():
        orm_mode = True


class CreateJob(JobBase):
    tasks: Optional[List[task_schema.Task]] = []
    class Config:
        schema_extra = {
            "example": {
                "name": "Lake house",
                "location": "24 lakeview rd",
                "details": "bathroom remodel",
                "is_complete": "False",
                "date": "2021-09-29",
                
            }
        }


class UpdateJob(JobBase):

    pass

