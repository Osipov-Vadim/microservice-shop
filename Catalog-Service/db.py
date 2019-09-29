from sqlalchemy.engine import create_engine
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker

class SQLAlchemy:
    def __init__(self):
        self.engine = None
        self.session = None
        self._db_uri = None

    def close(self):
        self.session.flush()
        self.session.close()

    def init_app(self, db_uri, is_debug=False):
        self._db_uri = db_uri
        self.engine = create_engine(self._db_uri, echo=is_debug)
        sm = sessionmaker(bind=self.engine)
        self.session = scoped_session(sm)