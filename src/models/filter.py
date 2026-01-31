from dataclasses import dataclass
from enum import Enum

from .structs import СomparisonType


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
    comprasion: СomparisonType
    value: int
    enabled: bool


@dataclass
class RoleKpiMetrics:
    positive_indicators: dict
    negative_indicators: dict


filter_kpi = {}

for r in KpiRole:
    positive_indicators = {
        "passes_percent": ValueIndicators(СomparisonType.EQUALLY, 0, False),
        "captures_percent": ValueIndicators(СomparisonType.EQUALLY, 0, False),
        "rakov_cleared": ValueIndicators(СomparisonType.EQUALLY, 0, False),
        "tackles_done": ValueIndicators(СomparisonType.EQUALLY, 0, False),
        "meters_covered": ValueIndicators(СomparisonType.EQUALLY, 0, False),
        "defenders_beaten": ValueIndicators(СomparisonType.EQUALLY, 0, False),
        "breakthroughs": ValueIndicators(СomparisonType.EQUALLY, 0, False),
        "attempts_grounded": ValueIndicators(СomparisonType.EQUALLY, 0, False),
        "realizations_percent": ValueIndicators(СomparisonType.EQUALLY, 0, False),
        "penalties_percent": ValueIndicators(СomparisonType.EQUALLY, 0, False),
        "dropgoals_percent": ValueIndicators(СomparisonType.EQUALLY, 0, False),
        "points_scored": ValueIndicators(СomparisonType.EQUALLY, 0, False),
    }
    negative_indicators = {
        "penalties_received": ValueIndicators(СomparisonType.EQUALLY, 0, False),
        "loss_ball": ValueIndicators(СomparisonType.EQUALLY, 0, False),
        "yellow_cards": ValueIndicators(СomparisonType.EQUALLY, 0, False),
        "red_cards": ValueIndicators(СomparisonType.EQUALLY, 0, False),
    }
    filter_kpi[r] = RoleKpiMetrics(positive_indicators, negative_indicators)
