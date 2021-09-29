from pathlib import Path

import fastapi
import uvicorn

from data import db_session
from routes import jobs

app = fastapi.FastAPI()

app.include_router(jobs.router)

def configure_db(dev_mode: bool):
    file = (Path(__file__).parent / 'db' / 'pypi.sqlite').absolute()
    db_session.global_init(file.as_posix())


if __name__ == "__main__":
    configure_db(dev_mode=True)
    uvicorn.run(app)