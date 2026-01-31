from sqlite3 import connect
from os import path, makedirs

data_path = "data"


def create_db():
    if not path.exists(data_path):
        makedirs("data")
    conn = connect("data\\base.db")
