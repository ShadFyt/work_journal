from fastapi import APIRouter

router = APIRouter(prefix="/jobs")


@router.get("/", tags=['jobs'])
async def show_all_jobs():
    return [
        {"loc": "24 ann rd"},
        {"loc": "26 lake ave"}
    ]

@router.get("/1", tags=["jobs"])
async def show_job():
    return {"loc": "26 lake ave"}

@router.post("/")
async def create_job():
    return "created new job"