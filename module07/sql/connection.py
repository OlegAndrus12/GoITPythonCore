import sqlite3
from contextlib import contextmanager


@contextmanager
def create_connection():
    """ create a database connection to a Postgres database """
    conn = None
    try:
        conn = sqlite3.connect("project.db")
        yield conn
        conn.commit()
    except Exception as err:
        print(err)
        conn.rollback()
    finally:
        conn.close()
