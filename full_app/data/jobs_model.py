import datetime
import sqlalchemy as sa

from data.modelbase import SqlAlchemyBase


class Job(SqlAlchemyBase):
    __tablename__ = 'jobs'
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)
    location = sa.Column(sa.String)
    details =sa.Column(sa.String, nullable=True)
    is_complete =sa.Column(sa.Boolean, default=False)
    date =sa.Column(sa.DateTime, default = datetime.datetime.now, index=True)


class Task(SqlAlchemyBase):
    __tablename__ = 'tasks'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    detail = sa.Column(sa.String)
    is_complete = sa.Column(sa.Boolean, default = False)
    
