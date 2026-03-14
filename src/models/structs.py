from dataclasses import dataclass
from datetime import date
from enum import Enum, IntEnum
from typing import Optional


class Role(IntEnum):
    FIRST_LINE = 1
    SECOND_LINE = 2
    THIRD_LINE = 3
    SCRUM_HALF = 4
    FLY_HALF = 5
    CENTER = 6
    WING = 7
    FULLBACK = 8
    NOTHING = 9


class ComparisonType(Enum):
    EQUALLY = "="
    LESS = ">"
    MORE = "<"
    EQUALLY_MORE = "=<"
    EQUALLY_LESS = ">="


@dataclass(order=True)
class Team:
    id: int
    name: str
    path_to_logo: str = ""


@dataclass(order=True)
class Player:
    id: int
    full_name: str
    weight: float
    height: float
    birth_date: date
    path_to_photo: str = ""


@dataclass
class Transfer:
    id: int
    player: Player
    team: Team
    date: date


@dataclass
class Game:
    id: int
    name: str
    first_team: Team
    second_team: Team


class ComparisonValue:
    def __init__(self, comparison_type: ComparisonType, value: int):
        self.comparison_type = comparison_type
        self.value = value


@dataclass
class AllStat:
    player_name: str
    team: int
    role: str
    game_id: int | None = None

    minutes_played: int = 0

    successful_passes: int = 0
    bad_passes: int = 0

    successful_tackle: int = 0
    dominant_tackles: int = 0
    miss_tackle: int = 0

    ruck_cleared: int = 0
    steals: int = 0

    metres_carried: int = 0
    defenders_beaten: int = 0
    carriers: int = 0

    line_breaks: int = 0
    line_break_assists: int = 0

    tries: int = 0
    try_assists: int = 0

    successful_conversions: int = 0
    successful_penalties: int = 0
    successful_drop_goal: int = 0

    miss_conversions: int = 0
    miss_penalties: int = 0
    miss_drop_goal: int = 0
    points: int = 0
    scrums_win: int = 0
    scrums_steal: int = 0
    scrums_lose: int = 0
    lineout_win: int = 0
    lineout_steal: int = 0
    lineout_lose: int = 0
    ball_losses: int = 0
    penalty: int = 0
    yellow_card: int = 0
    red_card: int = 0
