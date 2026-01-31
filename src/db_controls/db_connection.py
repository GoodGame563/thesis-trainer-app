from sqlite3 import Connection, connect

db_path = "data\\base.db"


def db_connect() -> Connection:
    return connect(db_path)
