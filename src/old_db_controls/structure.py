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
    __foreign_keys__: ClassVar[list[str]] = [
        "FOREIGN KEY (player_id) REFERENCES players(id)",
        "FOREIGN KEY (team_id) REFERENCES teams(id)",
        "FOREIGN KEY (role_id) REFERENCES roles(id)",
    ]

    id: int = pk()
    player_id: int = nn_int()
    team_id: int = nn_int()
    role_id: int = nn_int()
    minutes_played: int = nn_int()

    # ============= ПЕРЕДАЧИ =============
    successful_passes: int = nn_int()
    bad_passes: int = nn_int()

    # ============= ЗАХВАТЫ =============
    successful_tackle: int = nn_int()
    dominant_tackles: int = nn_int()
    miss_tackle: int = nn_int()

    # ============= РАКИ И ОТБОРЫ =============
    ruck_cleared: int = nn_int()
    steals: int = nn_int()

    # ============= ПРОНОС И ОБЫГРЫВАНИЕ =============
    metres_carried: int = nn_int()
    defenders_beaten: int = nn_int()
    carriers: int = nn_int()

    # ============= ПРОРЫВЫ =============
    line_breaks: int = nn_int()
    line_break_assists: int = nn_int()

    # ============= ПОПЫТКИ И АССИСТЫ =============
    tries: int = nn_int()
    try_assists: int = nn_int()

    # ============= УДАРЫ: УСПЕШНЫЕ =============
    successful_conversions: int = nn_int()
    successful_penalties: int = nn_int()
    successful_drop_goal: int = nn_int()

    # ============= УДАРЫ: НЕУДАЧНЫЕ =============
    miss_conversions: int = nn_int()
    miss_penalties: int = nn_int()
    miss_drop_goal: int = nn_int()

    # ============= ОЧКИ =============
    points: int = nn_int()

    # ============= СХВАТКИ =============
    scrums_win: int = nn_int()
    scrums_steal: int = nn_int()
    scrums_lose: int = nn_int()

    # ============= КОРИДОРЫ (ЛИНЕЙ-АУТЫ) =============
    lineout_win: int = nn_int()
    lineout_steal: int = nn_int()
    lineout_lose: int = nn_int()

    # ============= НАРУШЕНИЯ И ПОТЕРИ =============
    ball_losses: int = nn_int()
    penalty: int = nn_int()

    # ============= КАРТОЧКИ =============
    yellow_card: int = nn_int()
    red_card: int = nn_int()


@dataclass
class Transfers(TableSchema):
    __tablename__ = "transfers"
    __foreign_keys__: ClassVar[list[str]] = [
        "FOREIGN KEY (player_id) REFERENCES players(id)",
        "FOREIGN KEY (team_id) REFERENCES teams(id)",
    ]

    id: int = pk()
    player_id: int = nn_int()
    team_id: int = nn_int()
    date: str = nn_date()
