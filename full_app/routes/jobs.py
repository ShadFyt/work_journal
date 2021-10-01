
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from services import job_service
from schemas import job_schema

router = APIRouter(prefix="/jobs")


@router.get("/", tags=['jobs'])
async def show_all_jobs():
    results = await job_service.list_all_jobs()
    return results

@router.get("/{job_id}", tags=["jobs"])
async def show_job(job_id: int):
    return await job_service.show_job(job_id= job_id)


@router.post("/", response_model=job_schema.Job, status_code=201)
async def create_job(job: job_schema.CreateJob):
    return await job_service.create_job(job)


# async def create_job(job: job_schema.CreateJob):
#     job_dal = job_service.JobDal()
#     return await job_dal.create_job(job)

@router.put("/{job_id}", response_model=job_schema.Job)
async def update_job(job: job_schema.CreateJob, job_id: int):
    return await job_service.update_job(job = job, job_id= job_id)
