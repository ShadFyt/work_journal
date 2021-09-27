#crud operations for job routes
from typing import Optional, List
import sqlalchemy
from sqlalchemy.future import select
from sqlalchemy import func

from data.jobs_model import Job
from schemas.job_schema import CreateJob 


from data import db_session

async def get_jobs() -> List:
    async with db_session.create_async_session() as session:
        #query to db goes here
        query = select(Job).order_by(Job.date.desc())
        results = await session.execute(query)
        all_items = results.all()
        return list(all_items)
    

async def create_job(_job: CreateJob):
    job = Job()
    job.name = _job.name
    job.location = _job.location
    job.date = _job.start_date
    job.is_complete = _job.is_completed

    async with db_session.create_async_session() as session:
        session.add(job)
        await session.commit()
    return job


async def list_all_jobs():
    async with db_session.create_async_engine() as session:
        query = select(Job).all()