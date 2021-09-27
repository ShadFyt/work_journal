from fastapi import APIRouter

from services import job_service
from schemas import job_schema

router = APIRouter(prefix="/jobs")


@router.get("/", tags=['jobs'])
async def show_all_jobs() -> dict:
    results = await job_service.get_jobs()
    return results

@router.get("/1", tags=["jobs"])
async def show_job():
    return {"loc": "26 lake ave"}

@router.post("/", response_model=job_schema.Job)
async def create_job(job: job_schema.CreateJob):
    result = await job_service.create_job(job)
    return result