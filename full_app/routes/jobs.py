
from typing import List
from fastapi import APIRouter, Response, status


from services import job_service
from schemas import job_schema

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.get("/", response_model= List[job_schema.ShowJob])
async def show_all_jobs():
    results = await job_service.list_all_jobs()
    print(type(results[0]))
    return results

@router.get("/{job_id}", response_model= job_schema.ShowJob)
async def single_job(job_id: int, response: Response):
    result = await job_service.show_job(job_id= job_id)
    if not result:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"detail": f"job with the id of {job_id} does not exist"}

    return result




@router.post("/", response_model=job_schema.JobInDb, status_code=201)
async def new_job(job: job_schema.CreateJob):
    return await job_service.create_job(job)


# async def create_job(job: job_schema.CreateJob):
#     job_dal = job_service.JobDal()
#     return await job_dal.create_job(job)

@router.put("/{job_id}")
async def update_job(job: job_schema.CreateJob, job_id: int):
    result = await job_service.update_job(job = job, job_id= job_id)
    if not result:
        return {"detail": "Job not found"}
    
    return result
