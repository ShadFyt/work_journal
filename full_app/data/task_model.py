import sqlalchemy as sa
import sqlalchemy.orm as orm

from data.modelbase import SqlAlchemyBase


class Task(SqlAlchemyBase):
    __tablename__ = 'tasks'

    id = sa.Column(sa.Integer, primary_key=True)
    detail = sa.Column(sa.String, default="test")
    is_complete = sa.Column(sa.Boolean, default = False)
    
    job_id: int = sa.Column(sa.Integer, sa.ForeignKey("jobs.id"))
    job = orm.relation(
        "Job",
        single_parent=True,
        cascade="all, delete-orphan",
    )
