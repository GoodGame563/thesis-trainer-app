from dataclasses import dataclass
from datetime import date
from enum import Enum, IntEnum


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


class СomparisonType(Enum):
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




class ComparisonValue:
    def __init__(self, comparison_type: СomparisonType, value: int):
        self.comparison_type = comparison_type
        self.value = value
