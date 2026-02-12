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
    successful_passes: int = nn_int()      # Successful Passes × 1.25
    bad_passes: int = nn_int()             # Bad Passes × -0.3
    
    # ============= ЗАХВАТЫ =============
    successful_tackle: int = nn_int()      # Successful Tackle × 2.1
    dominant_tackles: int = nn_int()       # Dominant Tackles × 4.75
    miss_tackle: int = nn_int()            # Miss Tackle × -0.6
    
    # ============= РАКИ И ОТБОРЫ =============
    ruck_cleared: int = nn_int()           # Ruck cleared × 1.75
    steals: int = nn_int()                 # Steals × 5
    
    # ============= ПРОНОС И ОБЫГРЫВАНИЕ =============
    metres_carried: int = nn_int()         # Metres Carried × 0.9
    defenders_beaten: int = nn_int()       # Defenders Beaten × 2.5
    carriers: int = nn_int()               # Carriers × 1.75
    
    # ============= ПРОРЫВЫ =============
    line_breaks: int = nn_int()            # Line Breaks × 3.15
    line_break_assists: int = nn_int()     # Line Break assists × 1.2
    
    # ============= ПОПЫТКИ И АССИСТЫ =============
    tries: int = nn_int()                  # Tries × 5
    try_assists: int = nn_int()            # Try assists × 2.5
    
    # ============= УДАРЫ: УСПЕШНЫЕ =============
    successful_conversions: int = nn_int() # Successful Conversions × 2
    successful_penalties: int = nn_int()   # Successful Penalties × 3
    successful_drop_goal: int = nn_int()   # Successful Drop-goal × 5
    
    # ============= УДАРЫ: НЕУДАЧНЫЕ =============
    miss_conversions: int = nn_int()       # Miss Conversions × -0.2
    miss_penalties: int = nn_int()         # Miss Penalties × -1
    miss_drop_goal: int = nn_int()         # Miss Drop-goal × -5
    
    # ============= ОЧКИ =============
    points: int = nn_int()                 # Points × 1 (или × 2.5 - уточнить)
    
    # ============= СХВАТКИ =============
    scrums_win: int = nn_int()             # Scrums win × 1
    scrums_steal: int = nn_int()           # Scrums steal × 3
    scrums_lose: int = nn_int()            # Scrums lose × -1
    
    # ============= КОРИДОРЫ (ЛИНЕЙ-АУТЫ) =============
    lineout_win: int = nn_int()            # Lineout win × 1
    lineout_steal: int = nn_int()          # Lineout steal × 3
    lineout_lose: int = nn_int()           # Lineout lose × -1
    
    # ============= НАРУШЕНИЯ И ПОТЕРИ =============
    ball_losses: int = nn_int()            # Ball losses × -5
    penalty: int = nn_int()                # Penalty × -10
    
    # ============= КАРТОЧКИ =============
    yellow_card: int = nn_int()            # Yellow card × -20
    red_card: int = nn_int()               # Red card × -50


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
