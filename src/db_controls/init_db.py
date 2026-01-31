from os import makedirs, path
from sqlite3 import connect
from .structure import init_database

data_path = "data"


def create_db():
    if not path.exists(data_path):
        makedirs("data")
    init_database("data\\base.db")
