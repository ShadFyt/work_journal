
from fastapi import APIRouter

from services import job_service
from schemas import job_schema
from data import db_session

router = APIRouter(prefix="/jobs")


@router.get("/", tags=['jobs'])
async def show_all_jobs() -> dict:
    results = await job_service.list_all_jobs()
    return results

@router.get("/{job_id}", tags=["jobs"])
async def show_job(job_id: int):
    result = await job_service.show_job(job_id= job_id)
    return result

@router.post("/", response_model=job_schema.Job)
async def create_job(job: job_schema.CreateJob):
    result = await job_service.create_job(job)
    return result

# async def create_job(job: job_schema.CreateJob):
#     job_dal = job_service.JobDal()
#     return await job_dal.create_job(job)

@router.put("/{job_id}", response_model=job_schema.CreateJob)
async def update_job(job: job_schema.CreateJob, job_id: int):
    await job_service.update_job(job = job, job_id= job_id)