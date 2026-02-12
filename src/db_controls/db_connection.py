import aiosqlite

db_path = "data\\base.db"


def db_connect():
    return aiosqlite.connect(db_path)
