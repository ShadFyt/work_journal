#crud operations for job routes
from typing import Optional, List
from sqlalchemy.future import select

from data.jobs_model import Job
from schemas import job_schema
from data import db_session


# class JobDal():
#     def __init__(self):
#         pass

#     async def create_job(self,_job):
#         raw_data = _job
#         new_job = Job(**raw_data.dict())
#         async with db_session.create_async_session() as session:
#             session.add(new_job)
#             await session.flush()
        

async def list_all_jobs() -> List:
    async with db_session.create_async_session() as session:
        #query to db goes here
        query = select(Job).order_by(Job.date.desc())
        results = await session.execute(query)
        return results.scalars().all()
    

async def create_job(_job: job_schema.CreateJob):

    job = Job(**_job.dict())

    async with db_session.create_async_session() as session:
        session.add(job)
        await session.commit()
    return job


async def show_job(job_id: int):
    async with db_session.create_async_session() as session:
        query = select(Job).filter(Job.id == job_id)
        result = await session.execute(query)

        return result.scalar_one_or_none()

async def update_job(job_id: int, job: job_schema.CreateJob):
    async with db_session.create_async_session() as session:
        print(job)