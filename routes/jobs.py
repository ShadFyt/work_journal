from fastapi import APIRouter

router = APIRouter()


@router.get("/jobs/", tags=['jobs'])
async def show_all_jobs():
    return [
        {"loc": "24 ann rd"},
        {"loc": "26 lake ave"}
    ]

@router.get("/jobs/1", tags=["jobs"])
async def show_job():
    return {"loc": "26 lake ave"}

@router.post("/jobs/")
async def create_job():
    return "created new job"