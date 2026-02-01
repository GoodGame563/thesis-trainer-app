from dataclasses import dataclass, field, fields
from typing import ClassVar


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
    __foreign_keys__: ClassVar[list[str]] = []

    @classmethod
    def get_columns(cls) -> list[tuple[str, str]]:
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


@dataclass
class AllGames(TableSchema):
    __tablename__ = "all_games"
    __foreign_keys__ = [
        "FOREIGN KEY (player_id) REFERENCES players(id)",
        "FOREIGN KEY (team_id) REFERENCES teams(id)",
        "FOREIGN KEY (role_id) REFERENCES roles(id)",
    ]

    id: int = pk()
    player_id: int = nn_int()
    team_id: int = nn_int()
    role_id: int = nn_int()
    minutes_played: int = nn_int()
    passes_accurate: int = nn_int()
    passes_inaccurate: int = nn_int()
    passes_percent: float = nn_float()
    captures_done: int = nn_int()
    captures_missed: int = nn_int()
    captures_percent: float = nn_float()
    rakov_cleared: int = nn_int()
    tackles_done: int = nn_int()
    meters_covered: int = nn_int()
    defenders_beaten: int = nn_int()
    breakthroughs: int = nn_int()
    attempts_grounded: int = nn_int()
    realizations_scored: int = nn_int()
    realizations_attempted: int = nn_int()
    realizations_percent: float = nn_float()
    penalties_scored: int = nn_int()
    penalties_attempted: int = nn_int()
    penalties_percent: float = nn_float()
    dropgoals_scored: int = nn_int()
    dropgoals_attempted: int = nn_int()
    dropgoals_percent: float = nn_float()
    points_scored: int = nn_int()
    penalties_received: int = nn_int()
    loss_ball: int = nn_int()
    yellow_cards: int = nn_int()
    red_cards: int = nn_int()


@dataclass
class Transfers(TableSchema):
    __tablename__ = "transfers"
    __foreign_keys__ = [
        "FOREIGN KEY (player_id) REFERENCES players(id)",
        "FOREIGN KEY (team_id) REFERENCES teams(id)",
    ]

    id: int = pk()
    player_id: int = nn_int()
    team_id: int = nn_int()
    data: str = nn_date()
