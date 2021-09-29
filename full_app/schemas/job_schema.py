from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class JobBase(BaseModel):
    name: str
    location: str
    details: Optional[str] = None
    is_complete: bool = False
    date: date




class Job(JobBase):
    id: int

    class Config():
        orm_mode = True


class CreateJob(JobBase):
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Lake house",
                "location": "24 lakeview rd",
                "details": "bathroom remodel",
                "is_complete": "False",
                "date": "2021-09-29"
            }
        }


class UpdateJob(JobBase):

    pass

