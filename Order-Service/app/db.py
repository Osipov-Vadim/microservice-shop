import hug

from sqlalchemy.engine import create_engine
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker

from sqlalchemy.orm.session import Session


class SQLAlchemy:
    def __init__(self):
        self.engine = None
        self.session = None
        self._db_uri = None

    def close(self):
        self.session.flush()
        self.session.close()

    def init_app(self, db_uri):
        self._db_uri = db_uri
        self.engine = create_engine(self._db_uri, echo=False)
        sm = sessionmaker(bind=self.engine)
        self.session = scoped_session(sm)


class SQLAlchemyContext(object):
    def __init__(self, db: SQLAlchemy):
        self._db = db.session()

    @property
    def db(self) -> Session:
        return self._db

    def cleanup(self, exception=None):
        if exception:
            self.db.rollback()
            return

        self.db.commit()


@hug.directive()
class SQlAlchemySession(Session):
    def __new__(cls, *args, context: SQLAlchemyContext = None, **kwargs):
        return context.db
