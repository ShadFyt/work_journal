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
    pass

