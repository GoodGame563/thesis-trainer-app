from sqlite3 import connect
from dataclasses import dataclass, fields, field
from typing import ClassVar, List, Tuple


def pk():
    return field(metadata={"_sql": "INTEGER PRIMARY KEY"})


def nn_int():
    return field(metadata={"_sql": "INTEGER NOT NULL"})


def nn_str():
    return field(metadata={"_sql": "TEXT NOT NULL"})


def nn_float():
    return field(metadata={"_sql": "REAL NOT NULL"})


def nn_date():
    return field(metadata={"_sql": "DATE NOT NULL"})


class TableSchema:
    __tablename__: ClassVar[str] = ""
    __foreign_keys__: ClassVar[List[str]] = []

    @classmethod
    def get_columns(cls) -> List[Tuple[str, str]]:
        return [
            (f.name, f.metadata["_sql"]) for f in fields(cls) if "_sql" in f.metadata
        ]


@dataclass
class Players(TableSchema):
    __tablename__ = "players"
    id: int = pk()
    full_name: str = nn_str()
    height: int = nn_int()
    weight: int = nn_int()
    date_birth: str = nn_date()
    foto: str = nn_str()


@dataclass
class Teams(TableSchema):
    __tablename__ = "teams"

    id: int = pk()
    name: str = nn_str()
    logo: str = nn_str()


@dataclass
class Roles(TableSchema):
    __tablename__ = "roles"

    id: int = pk()
    name: str = nn_str()
