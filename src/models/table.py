from dataclasses import dataclass
from datetime import date

from .structs import Player, Role, Team

name_column_table = {
    "player": "Игрок",
    "date_birth": "Дата рождения",
    "team": "Команда",
    "role": "Амплуа",
    "minutes_played": "Минут сыграно",
    "successful_passes": "Точных передач",
    "bad_passes": "Неточных передач",
    "successful_tackle": "Успешных захватов",
    "dominant_tackles": "Подавляющих захватов",
    "miss_tackle": "Неуспешных захватов",
    "ruck_cleared": "Раков зачищено",
    "steals": "Мячей отобрано",
    "metres_carried": "Метров пройдено с мячом",
    "defenders_beaten": "Защитников обыграно",
    "carriers": "Входов в линию защиты",
    "line_breaks": "Прорывов линии обороны",
    "line_break_assists": "Ассистов прорывов",
    "tries": "Попыток занесено",
    "try_assists": "Ассистов попыток",
    "successful_conversions": "Точных реализаций",
    "successful_penalties": "Точных штрафных",
    "successful_drop_goal": "Точных дроп-голов",
    "miss_conversions": "Неточных реализаций",
    "miss_penalties": "Неточных штрафных",
    "miss_drop_goal": "Неточных дроп-голов",
    "points": "Очков набрано",
    "scrums_win": "Выигранных своих схваток",
    "scrums_steal": "Выигранных схваток соперника",
    "scrums_lose": "Проигранных своих схваток",
    "lineout_win": "Выигранных своих коридоров",
    "lineout_steal": "Выигранных коридоров соперника",
    "lineout_lose": "Проигранных своих коридоров",
    "ball_losses": "Потерь мяча",
    "penalty": "Штрафных получено",
    "yellow_card": "Жёлтых карточек",
    "red_card": "Красных карточек",
    "rating": "Рейтинговые баллы",
}


@dataclass(order=True)
class TableData:
    player: Player
    role: Role
    team: str
    date_birth: date
    minutes_played: int

    # ============= ПЕРЕДАЧИ =============
    successful_passes: int
    bad_passes: int

    # ============= ЗАХВАТЫ =============
    successful_tackle: int
    dominant_tackles: int
    miss_tackle: int

    # ============= РАКИ И ОТБОРЫ =============
    ruck_cleared: int
    steals: int

    # ============= ПРОНОС И ОБЫГРЫВАНИЕ =============
    metres_carried: int
    defenders_beaten: int
    carriers: int

    # ============= ПРОРЫВЫ =============
    line_breaks: int
    line_break_assists: int

    # ============= ПОПЫТКИ И АССИСТЫ =============
    tries: int
    try_assists: int

    # ============= УДАРЫ: УСПЕШНЫЕ =============
    successful_conversions: int
    successful_penalties: int
    successful_drop_goal: int

    # ============= УДАРЫ: НЕУДАЧНЫЕ =============
    miss_conversions: int
    miss_penalties: int
    miss_drop_goal: int

    # ============= ОЧКИ =============
    points: int

    # ============= СХВАТКИ =============
    scrums_win: int
    scrums_steal: int
    scrums_lose: int

    # ============= КОРИДОРЫ (ЛИНЕЙ-АУТЫ) =============
    lineout_win: int
    lineout_steal: int
    lineout_lose: int

    # ============= НАРУШЕНИЯ И ПОТЕРИ =============
    ball_losses: int
    penalty: int

    # ============= КАРТОЧКИ =============
    yellow_card: int
    red_card: int

    rating: float


@dataclass(order=True)
class ShortTableData:
    role: Role
    role: Role
    minutes_played: int
    # ============= ПЕРЕДАЧИ =============
    successful_passes: int
    bad_passes: int

    # ============= ЗАХВАТЫ =============
    successful_tackle: int
    dominant_tackles: int
    miss_tackle: int

    # ============= РАКИ И ОТБОРЫ =============
    ruck_cleared: int
    steals: int

    # ============= ПРОНОС И ОБЫГРЫВАНИЕ =============
    metres_carried: int
    defenders_beaten: int
    carriers: int

    # ============= ПРОРЫВЫ =============
    line_breaks: int
    line_break_assists: int

    # ============= ПОПЫТКИ И АССИСТЫ =============
    tries: int
    try_assists: int

    # ============= УДАРЫ: УСПЕШНЫЕ =============
    successful_conversions: int
    successful_penalties: int
    successful_drop_goal: int

    # ============= УДАРЫ: НЕУДАЧНЫЕ =============
    miss_conversions: int
    miss_penalties: int
    miss_drop_goal: int

    # ============= ОЧКИ =============
    points: int

    # ============= СХВАТКИ =============
    scrums_win: int
    scrums_steal: int
    scrums_lose: int

    # ============= КОРИДОРЫ (ЛИНЕЙ-АУТЫ) =============
    lineout_win: int
    lineout_steal: int
    lineout_lose: int

    # ============= НАРУШЕНИЯ И ПОТЕРИ =============
    ball_losses: int
    penalty: int

    # ============= КАРТОЧКИ =============
    yellow_card: int
    red_card: int

    rating: float
