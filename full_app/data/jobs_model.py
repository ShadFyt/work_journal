import datetime
from typing import List
import sqlalchemy as sa
import sqlalchemy.orm as orm

# from data.task_model import Task
from data.modelbase import SqlAlchemyBase


class Job(SqlAlchemyBase):
    __tablename__ = 'jobs'
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)
    location = sa.Column(sa.String)
    details =sa.Column(sa.String, nullable=True)
    is_complete =sa.Column(sa.Boolean, default=False)
    date =sa.Column(sa.DateTime, default = datetime.datetime.now, index=True)

    tasks = orm.relation(
        "Task",
        back_populates="job",
    )