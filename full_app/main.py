from pathlib import Path

import fastapi
import uvicorn

from data import db_session
from schemas import task_schema
from services.task_service import create_job_task
from routes import jobs, task_route

app = fastapi.FastAPI()

app.include_router(jobs.router)
app.include_router(task_route.router)

def configure_db(dev_mode: bool):
    file = (Path(__file__).parent / 'db' / 'test.sqlite').absolute()
    db_session.global_init(file.as_posix())



if __name__ == "__main__":
    configure_db(dev_mode=True)

    uvicorn.run(app)
