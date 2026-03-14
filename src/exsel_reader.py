from typing import List, Optional

import pandas as pd

from models import AllStat


def parse_excel_to_stats(file_path: str, game_id: int | None = None) -> list[AllStat]:
    df = pd.read_excel(file_path, sheet_name="primer", header=0)

    column_map = {
        "Игрок": "player_name",
        "Команда": "team",
        "Роль": "role",
        "Минуты": "minutes_played",
        "Успешные передачи": "successful_passes",
        "Плохие передачи": "bad_passes",
        "Успешные захваты": "successful_tackle",
        "Доминирующие захваты": "dominant_tackles",
        "Промахи в захватах": "miss_tackle",
        "Рак очищен": "ruck_cleared",
        "Отборы": "steals",
        "Метры выноса": "metres_carried",
        "Обыгранные защитники": "defenders_beaten",
        "Выносы": "carriers",
        "Прорывы": "line_breaks",
        "Ассисты прорыва": "line_break_assists",
        "Попытки": "tries",
        "Ассисты попытки": "try_assists",
        "Успешные конверсии": "successful_conversions",
        "Успешные штрафы": "successful_penalties",
        "Успешные дроп-голы": "successful_drop_goal",
        "Промах конверсии": "miss_conversions",
        "Промах штрафы": "miss_penalties",
        "Промах дроп-гол": "miss_drop_goal",
        "Очки": "points",
        "Схватка выиграна": "scrums_win",
        "Схватка украдена": "scrums_steal",
        "Схватка проиграна": "scrums_lose",
        "Коридор выигран": "lineout_win",
        "Коридор украден": "lineout_steal",
        "Коридор проигран": "lineout_lose",
        "Потери мяча": "ball_losses",
        "Штрафы": "penalty",
        "Желтые карточки": "yellow_card",
        "Красные карточки": "red_card",
    }

    mapped_df = pd.DataFrame()
    for rus_col, eng_field in column_map.items():
        if rus_col in df.columns:
            mapped_df[eng_field] = df[rus_col]

    str_columns = ["player_name", "team", "role"]
    numeric_columns = [col for col in mapped_df.columns if col not in str_columns]

    mapped_df[str_columns] = mapped_df[str_columns].fillna("").astype(str)
    mapped_df[numeric_columns] = mapped_df[numeric_columns].fillna(0).astype(int)

    stats_list: list[AllStat] = []
    for _, row in mapped_df.iterrows():
        player_name = row["player_name"].strip()
        if not player_name:
            continue

        row_dict = row.to_dict()
        instance = AllStat(game_id=game_id, **row_dict)

        stats_list.append(instance)

    return stats_list
