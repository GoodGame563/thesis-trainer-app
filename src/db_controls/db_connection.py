from sqlite3 import connect, Connection

db_path = "data\\base.db"

def db_connect() -> Connection:
    return connect(db_path)
