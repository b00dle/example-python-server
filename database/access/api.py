from database import base
from sqlalchemy import exc
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()


class Api(object):
    def __init__(self, bind):
        self._db = None
        self.bind = bind

    def open(self):
        """ creates a session for database transaction if none is active. """
        if not self.is_open():
            self._db = Session(bind=self.bind)
        else:
            ValueError("FAILURE: Session is already open.")

    def close(self):
        """ closes the current database session if open. """
        if self.is_open():
            self._db.expunge_all()
            self._db.close()
            self._db = None
        else:
            ValueError("FAILURE: No Session to close.")

    def _clear(self):
        """ clears all tables """
        for table in reversed(base.TableBase.metadata.sorted_tables):
            self._db.execute(table.delete())
        return self.commit()

    def commit(self):
        """ Commits changed content left in session.
            Automatic rollback is performed if errror occurs. """
        if self.is_open():
            try:
                self._db.commit()
            except exc.SQLAlchemyError as e:
                self._db.rollback()
                raise e
        else:
            raise ValueError("FAILURE: Session has not been opened.")

    def is_open(self):
        """ Returns true if the current session is active, false otherwise. """
        return self._db is not None

    def insert(self, obj):
        """ adds a database object to the current session. """
        self._db.add(obj)

    def insert_all(self, obj_list):
        """ adds a list of database objects to the current session. """
        self._db.add_all(obj_list)

    def expunge(self, obj):
        """ removes a database object from the current session. """
        self._db.expunge(obj)

    def expunge_all(self, obj_list):
        """ removes a list of database objects from the current session. """
        for item in obj_list:
            self._db.expunge(item)

    def delete(self, obj):
        """ Helper function to encapsulate delete operations. """
        self._db.delete(obj)

    def query(self, *args):
        """ universal function for querying the database connection. """
        return self._db.query(*args)

    def select(self, table, filter=None):
        """ helper function for performing simple select operations. """
        if filter is None:
            return self.query(table)
        return self.query(table).filter(filter)
