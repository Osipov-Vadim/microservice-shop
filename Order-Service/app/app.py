import hug

from db import SQLAlchemy, SQLAlchemyContext, SQlAlchemySession
from models.base import Base
import routers

database = SQLAlchemy()
database.init_app("sqlite:///orders.db")
Base.metadata.create_all(bind=database.engine)


@hug.context_factory()
def create_context(*args, **kwargs):
    return SQLAlchemyContext(database)


@hug.delete_context()
def delete_context(
        context: SQLAlchemyContext, exception=None, errors=None, lacks_requirement=None):
    context.cleanup(exception)


@hug.extend_api()
def apis():
    return [routers]
