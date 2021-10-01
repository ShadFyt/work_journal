from fastapi import APIRouter


from schemas import task_schema
from services import task_service


router = APIRouter(prefix="/jobs/{job_id}/tasks")

@router.post("/", status_code= 201, response_model=task_schema.CreateTask)
async def create_task(task: task_schema.CreateTask ,job_id:int):
    return await task_service.create_job_task(task, job_id)


@router.get("/")
async def list_task_by_job(job_id:int):
    return await task_service.list_task_by_job_id(job_id=job_id)