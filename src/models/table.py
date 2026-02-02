from dataclasses import dataclass
from datetime import date

from .structs import Player, Role, Team

name_column_table = {
    "player": "Игрок",
    "date_birth": "Дата рождения",
    "team": "Команда",
    "role": "Амплуа",
    "minutes_played": "Минут сыграно",
    "passes_accurate": "Передач отдано (точных)",
    "passes_inaccurate": "Передач не точных",
    "passes_percent": "% точности передач",
    "captures_done": "Захватов выполнено",
    "captures_missed": "Захватов мимо",
    "captures_percent": "% захватов",
    "rakov_cleared": "Раков зачищено",
    "tackles_done": "Отборов выполнено",
    "meters_covered": "Метров пройдено",
    "defenders_beaten": "Защитников обыграно",
    "breakthroughs": "Прорывов",
    "attempts_grounded": "Попыток занесено",
    "realizations_scored": "Реализаций забито",
    "realizations_attempted": "Реализаций пробивалось",
    "realizations_percent": "% точности реализаций",
    "penalties_scored": "Штрафных забито",
    "penalties_attempted": "Штрафных пробивалось",
    "penalties_percent": "% точности штрафных",
    "dropgoals_scored": "Дроп-голов забито",
    "dropgoals_attempted": "Дроп-голов пробивалось",
    "dropgoals_percent": "% точности Дроп-голов",
    "points_scored": "Очков набрано",
    "penalties_received": "Штрафных получено",
    "loss_ball": "Потерь мяча",
    "yellow_cards": "Желтых карточек",
    "red_cards": "Красных карточек",
    "rating": "Рейтинговые баллы",
}


@dataclass
class TableData:
    player: Player
    role: Role
    minutes_played: int
    passes_accurate: int
    passes_inaccurate: int
    passes_percent: float
    captures_done: int
    captures_missed: int
    captures_percent: float
    rakov_cleared: int
    tackles_done: int
    meters_covered: int
    defenders_beaten: int
    breakthroughs: int
    attempts_grounded: int
    realizations_scored: int
    realizations_attempted: int
    realizations_percent: float
    penalties_scored: int
    penalties_attempted: int
    penalties_percent: float
    dropgoals_scored: int
    dropgoals_attempted: int
    dropgoals_percent: float
    points_scored: int
    penalties_received: int
    loss_ball: int
    yellow_cards: int
    red_cards: int
    rating: float


def create_empty() -> TableData:
    return TableData(
        player=Player(
            nst="Иванов Иван Иванович",
            weight=85.0,
            height=190.0,
            team=Team(name="Рубин"),
            birth_date=date(1995, 5, 15),
        ),
        role=Role.NOTHING,
        minutes_played=0,
        passes_accurate=0,
        passes_inaccurate=0,
        captures_done=0,
        captures_missed=0,
        rakov_cleared=0,
        tackles_done=0,
        meters_covered=0,
        defenders_beaten=0,
        breakthroughs=0,
        attempts_grounded=0,
        realizations_scored=0,
        realizations_attempted=0,
        penalties_scored=0,
        penalties_attempted=0,
        dropgoals_scored=0,
        dropgoals_attempted=0,
        points_scored=0,
        penalties_received=0,
        loss_ball=0,
        yellow_cards=0,
        red_cards=0,
        passes_percent=0.0,
        captures_percent=0.0,
        realizations_percent=0.0,
        penalties_percent=0.0,
        dropgoals_percent=0.0,
        rating=0.0,
    )
