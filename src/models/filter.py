from dataclasses import dataclass
from enum import Enum

from .structs import ComparisonType


class KpiRole(Enum):
    FIRST_LINE = "Первая линия"
    SECOND_LINE = "Вторая линия"
    THIRD_LINE = "Третья линия"
    SCRUM_HALF = "Полузащитник схватки"
    FLY_HALF = "Полузащитник веера"
    CENTER = "Центр"
    WING = "Крайний"
    FULLBACK = "Фуллбэк"
    ALL_ROLES = "Все роли"


@dataclass
class ValueIndicators:
    comprasion: ComparisonType
    value: int
    enabled: bool


@dataclass
class RoleKpiMetrics:
    positive_indicators: dict
    negative_indicators: dict


filter_kpi = {}

for r in KpiRole:
    positive_indicators = {
        "successful_passes": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "successful_tackle": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "dominant_tackles": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "ruck_cleared": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "steals": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "metres_carried": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "defenders_beaten": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "carriers": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "line_breaks": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "line_break_assists": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "tries": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "try_assists": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "successful_conversions": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "successful_penalties": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "successful_drop_goal": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "points": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "scrums_win": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "scrums_steal": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "lineout_win": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "lineout_steal": ValueIndicators(ComparisonType.EQUALLY, 0, False),
    }
    negative_indicators = {
        "ball_losses": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "penalty": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "yellow_card": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "red_card": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "bad_passes": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "miss_tackle": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "miss_conversions": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "miss_penalties": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "miss_drop_goal": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "scrums_lose": ValueIndicators(ComparisonType.EQUALLY, 0, False),
        "lineout_lose": ValueIndicators(ComparisonType.EQUALLY, 0, False),
    }
    filter_kpi[r] = RoleKpiMetrics(positive_indicators, negative_indicators)
