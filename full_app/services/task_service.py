from fastapi.encoders import jsonable_encoder
from sqlalchemy.future import select
from typing import List

from data import db_session
from data.task_model import Task
from data.jobs_model import Job
from schemas import task_schema

async def create_job_task(task: task_schema.CreateTask ,job_id: int ):

    async with db_session.create_async_session() as session:
        new_task = Task(**task.dict(), job_id=job_id)
        session.add(new_task)
        await session.commit()
        return new_task

async def list_task_by_job_id(job_id:int) -> List[task_schema.ShowTask]:
    async with db_session.create_async_session() as session:
        query = select(Task).where(Task.job_id == job_id)
        result = await session.execute(query)
        return result.scalars().all()





