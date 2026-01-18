from enum import Enum
from datetime import date


class Role(Enum):
    FIRST_LINE = "Первая линия"
    SECOND_LINE = "Вторая линия"
    THIRD_LINE = "Третья линия"
    SCRUM_HALF = "Полузащитник схватки"
    FLY_HALF = "Полузащитник веера"
    CENTER = "Центр"
    WING = "Крайний"
    FULLBACK = "Фуллбэк"
    NOTHING = "Не указано"


class ButtonType(Enum):
    ACTION = 1
    BASIC = 2
    AGREE = 3
    CANCEL = 4


class Team:
    def __init__(self, name: str, path_to_logo: str = ""):
        self.path_to_logo = path_to_logo
        self.name = name


class Player:
    def __init__(
        self,
        nst: str,
        weight: float,
        height: float,
        team: Team,
        birth_date: date,
        path_to_photo: str = "",
    ):
        self.full_name = nst
        self.weight = weight
        self.height = height
        self.path_to_photo = path_to_photo
        self.team = team
        self.birth_date = birth_date
