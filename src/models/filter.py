from dataclasses import dataclass
from enum import Enum

from aioshutil import R

from .structs import ComparisonType, Role
from .table import TableData


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

positive_multipliers = {
    "successful_passes": 1.25,
    "successful_tackle": 2.1,
    "dominant_tackles": 4.75,
    "ruck_cleared": 1.75,
    "steals": 5,
    "metres_carried": 0.9,
    "defenders_beaten": 2.5,
    "carriers": 1.75,
    "line_breaks": 3.15,
    "line_break_assists": 1.2,
    "tries": 5,
    "try_assists": 2.5,
    "successful_conversions": 2,
    "successful_penalties": 3,
    "successful_drop_goal": 5,
    "points": 1,
    "scrums_win": 1,
    "scrums_steal": 3,
    "lineout_win": 1,
    "lineout_steal": 3,
}

negative_multipliers = {
    "ball_losses": -5,
    "penalty": -10,
    "yellow_card": -20,
    "red_card": -50,
    "bad_passes": -0.3,
    "miss_tackle": -0.6,
    "miss_conversions": -0.2,
    "miss_penalties": -1,
    "miss_drop_goal": -5,
    "scrums_lose": -1,
    "lineout_lose": -1,
}

role_bonus = {
    KpiRole.FIRST_LINE: [
        "ruck_cleared",
        "successful_tackle",
        "dominant_tackles",
        "line_breaks",
    ],
    KpiRole.SECOND_LINE: [
        "ruck_cleared",
        "successful_tackle",
        "dominant_tackles",
        "steals",
        "metres_carried",
    ],
    KpiRole.THIRD_LINE: [
        "successful_tackle",
        "dominant_tackles",
        "steals",
        "line_breaks",
        "ruck_cleared",
    ],
    KpiRole.SCRUM_HALF: ["all"],
    KpiRole.FLY_HALF: [
        "successful_passes",
        "successful_conversions",
        "successful_penalties",
        "successful_drop_goal",
        "metres_carried",
        "points",
    ],
    KpiRole.CENTER: [
        "defenders_beaten",
        "line_breaks",
        "successful_passes",
        "successful_tackle",
        "dominant_tackles",
    ],
    KpiRole.WING: ["metres_carried", "defenders_beaten", "line_breaks"],
    KpiRole.FULLBACK: ["all", "-ruck_cleared"],
}

compare_kpi_role = {
    Role.FIRST_LINE: KpiRole.FIRST_LINE,
    Role.SECOND_LINE: KpiRole.SECOND_LINE,
    Role.THIRD_LINE: KpiRole.THIRD_LINE,
    Role.SCRUM_HALF: KpiRole.SCRUM_HALF,
    Role.FLY_HALF: KpiRole.FLY_HALF,
    Role.CENTER: KpiRole.CENTER,
    Role.WING: KpiRole.WING,
    Role.FULLBACK: KpiRole.FULLBACK,
}


def role_changed(role: KpiRole) -> bool:
    for p_i in filter_kpi[role].positive_indicators.values():
        if p_i.enabled:
            return True
    return any(p_i.enabled for p_i in filter_kpi[role].negative_indicators.values())


def calculate_bonus(data: TableData) -> int:
    bonus = 0
    if data.bad_passes == 0 and data.successful_passes >= 10:
        bonus += 50
    if data.miss_tackle == 0 and data.successful_tackle >= 5:
        bonus += 50
    if data.penalty == 0:
        bonus += 100
    if data.ruck_cleared >= 15:
        bonus += 50
    if data.line_breaks >= 5:
        bonus += 50
    if data.steals >= 5:
        bonus += 100
    if data.metres_carried >= 300:
        bonus += 50
    return bonus


def anything_changed() -> bool:
    for role in KpiRole:
        for p_i in filter_kpi[role].positive_indicators.values():
            if p_i.enabled:
                return True
        for p_i in filter_kpi[role].negative_indicators.values():
            if p_i.enabled:
                return True
    return False


async def calculate_kpi(role_selected: bool, data: TableData) -> TableData:
    rating = 0.0
    kpi_role = compare_kpi_role[data.role]
    success_rules = 0
    needs_rules = 0
    if role_changed(kpi_role):
        select_filter_kpi = filter_kpi[kpi_role]
    else:
        select_filter_kpi = filter_kpi[KpiRole.ALL_ROLES]

    for key, value in select_filter_kpi.positive_indicators.items():
        if value.enabled:
            needs_rules += 1
            data_in_cell = getattr(data, key)
            compare_value = int(value.value)
            print(
                f"{key}: данные в табличке {data_in_cell} {value.comprasion.value} данные в строке {compare_value}"
            )
            if bool(f"{data_in_cell}{value.comprasion.value}{compare_value}"):
                success_rules += 1
                if (
                    role_selected
                    and (key in role_bonus[kpi_role] or "all" in role_bonus[kpi_role])
                    and f"-{key}" not in role_bonus[kpi_role]
                ):
                    rating += positive_multipliers[key] * 2 * data_in_cell
                else:
                    rating += positive_multipliers[key] * data_in_cell

    for key, value in select_filter_kpi.negative_indicators.items():
        if value.enabled:
            data_in_cell = getattr(data, key)
            compare_value = int(value.value)
            print(
                f"{key}:  данные в табличке {data_in_cell} {value.comprasion.value} данные в строке {compare_value}"
            )
            print("рейтинг до: ", rating)
            if bool(f"{data_in_cell}{value.comprasion.value}{compare_value}"):
                rating += negative_multipliers[key] * data_in_cell
            print("рейтинг после: ", rating)

    rating = (
        rating * (0.75 + (success_rules / needs_rules) * 0.5) + calculate_bonus(data)
    ) / data.minutes_played
    print(rating)
    data.rating = rating
    return data
