from flet import (
    DataCell,
    DataColumn,
    DataRow,
    DataTable,
    Text,
    BorderSide,
    ColorScheme,
    CupertinoFilledButton,
)
from structs import Role, Player, Team
from datetime import date
from utils import create_basic_text, create_basic_text_button

visible_column_table = {
    "player": True,
    "date_birth": True,
    "team": True,
    "role": True,
    "minutes_played": True,
    "passes_accurate": True,
    "passes_inaccurate": True,
    "passes_percent": True,
    "captures_done": True,
    "captures_missed": True,
    "captures_percent": True,
    "rakov_cleared": True,
    "tackles_done": True,
    "meters_covered": True,
    "defenders_beaten": True,
    "breakthroughs": True,
    "attempts_grounded": True,
    "realizations_scored": True,
    "realizations_attempted": True,
    "realizations_percent": True,
    "penalties_scored": True,
    "penalties_attempted": True,
    "penalties_percent": True,
    "dropgoals_scored": True,
    "dropgoals_attempted": True,
    "dropgoals_percent": True,
    "points_scored": True,
    "penalties_received": True,
    "loss_ball": True,
    "yellow_cards": True,
    "red_cards": True,
    "rating": True,
}

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

positive_indicators = {
    "passes_percent": None,
    "captures_percent": None,
    "rakov_cleared": None,
    "tackles_done": None,
    "meters_covered": None,
    "defenders_beaten": None,
    "breakthroughs": None,
    "attempts_grounded": None,
    "realizations_percent": None,
    "penalties_percent": None,
    "dropgoals_percent": None,
    "points_scored": None,
}

negative_indicators = {
    "penalties_received": None,
    "loss_ball": None,
    "yellow_cards": None,
    "red_cards": None,
}




class TableData:
    def __init__(
        self,
        player: Player,
        role: Role,
        minutes_played: int,
        passes_accurate: int,
        passes_inaccurate: int,
        passes_percent: float,
        captures_done: int,
        captures_missed: int,
        captures_percent: float,
        rakov_cleared: int,
        tackles_done: int,
        meters_covered: int,
        defenders_beaten: int,
        breakthroughs: int,
        attempts_grounded: int,
        realizations_scored: int,
        realizations_attempted: int,
        realizations_percent: float,
        penalties_scored: int,
        penalties_attempted: int,
        penalties_percent: float,
        dropgoals_scored: int,
        dropgoals_attempted: int,
        dropgoals_percent: float,
        points_scored: int,
        penalties_received: int,
        loss_ball: int,
        yellow_cards: int,
        red_cards: int,
    ):
        self.player = player
        self.date_birth = player.birth_date
        self.team = player.team.name
        self.role = role
        self.minutes_played = minutes_played
        self.passes_accurate = passes_accurate
        self.passes_inaccurate = passes_inaccurate
        self.passes_percent = passes_percent
        self.captures_done = captures_done
        self.captures_missed = captures_missed
        self.captures_percent = captures_percent
        self.rakov_cleared = rakov_cleared
        self.tackles_done = tackles_done
        self.meters_covered = meters_covered
        self.defenders_beaten = defenders_beaten
        self.breakthroughs = breakthroughs
        self.attempts_grounded = attempts_grounded
        self.realizations_scored = realizations_scored
        self.realizations_attempted = realizations_attempted
        self.realizations_percent = realizations_percent
        self.penalties_scored = penalties_scored
        self.penalties_attempted = penalties_attempted
        self.penalties_percent = penalties_percent
        self.dropgoals_scored = dropgoals_scored
        self.dropgoals_attempted = dropgoals_attempted
        self.dropgoals_percent = dropgoals_percent
        self.points_scored = points_scored
        self.penalties_received = penalties_received
        self.loss_ball = loss_ball
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards
        self.rating = 0.0


def create_empty() -> TableData:
    return TableData(
        player=Player(
            nst="Иванов Иван Иванович",
            weight=85.0,
            height=190.0,
            team=Team(name="Рубин"),
            birth_date=date(1990, 5, 15),
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
    )


def create_table(
    data_list: list[TableData],
    color_scheme: ColorScheme,
    visible_column_table: dict[str, bool],
) -> DataTable:
    columns = []
    for key, value in visible_column_table.items():
        columns.append(
            DataColumn(
                create_basic_text(f"{name_column_table[key]}"), visible=value, key=key
            )
        )
    rows = []
    for d in data_list:
        cells = []
        for a in visible_column_table:
            if a == "player":
                button = create_basic_text_button(getattr(d, a).full_name, color_scheme)
                button.margin = 5
                cells.append(
                    DataCell(
                        button,
                        visible=visible_column_table[a],
                        key=a,
                    )
                )
                continue
            cells.append(
                DataCell(
                    create_basic_text(getattr(d, a)),
                    visible=visible_column_table[a],
                    key=a,
                )
            )

        rows.append(DataRow(cells=cells))

    return DataTable(
        columns=columns,
        rows=rows,
        expand=False,
        horizontal_lines=BorderSide(1, color_scheme.outline),
        vertical_lines=BorderSide(1, color_scheme.outline),
        show_bottom_border=True,
        clip_behavior="hard",
        border_radius=9,
        column_spacing=8,
        divider_thickness=1,
    )


def update_table(dataTable: DataTable):
    for i in range(len(dataTable.columns)):
        value = visible_column_table[dataTable.columns[i].key]
        dataTable.columns[i].visible = value
        for row in dataTable.rows:
            row.cells[i].visible = value
