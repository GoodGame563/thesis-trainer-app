from flet import DataCell, DataColumn, DataRow, DataTable, Text, BorderSide,ColorScheme, CupertinoFilledButton
from structs import Role, Player
from datetime import date

class TableData:
    def __init__(self, player: Player, date_birth: date, role:Role, minutes_played: int,
                 passes_accurate: int, passes_inaccurate: int, passes_percent: float,
                 captures_done:int, captures_missed:int, captures_percent: float,
                 rakov_cleared:int, tackles_done:int,
                 meters_covered:int, defenders_beaten:int,
                 breakthroughs:int, attempts_grounded:int,
                 realizations_scored:int, realizations_attempted:int, realizations_percent: float,
                 penalties_scored:int, penalties_attempted:int, penalties_percent: float,
                 dropgoals_scored:int, dropgoals_attempted:int, dropgoals_percent: float, 
                 points_scored:int, penalties_received:int,
                 turnovers:int, yellow_cards:int, red_cards:int):
        self.player = player
        self.date_birth = date_birth    
        self.team = player.team.name
        self.role = role
        self.minutes_played = minutes_played
        self.passes_accurate = passes_accurate
        self.passes_inaccurate = passes_inaccurate
        self.captures_done = captures_done
        self.captures_missed = captures_missed
        self.rakov_cleared = rakov_cleared
        self.tackles_done = tackles_done
        self.meters_covered = meters_covered
        self.defenders_beaten = defenders_beaten
        self.breakthroughs = breakthroughs
        self.attempts_grounded = attempts_grounded
        self.realizations_scored = realizations_scored
        self.realizations_attempted = realizations_attempted
        self.penalties_scored = penalties_scored
        self.penalties_attempted = penalties_attempted
        self.dropgoals_scored = dropgoals_scored
        self.dropgoals_attempted = dropgoals_attempted
        self.points_scored = points_scored
        self.penalties_received = penalties_received
        self.turnovers = turnovers
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards
        self.passes_percent = passes_percent
        self.captures_percent = captures_percent    
        self.realizations_percent = realizations_percent
        self.penalties_percent = penalties_percent
        self.dropgoals_percent = dropgoals_percent
        self.rating = 0.0

def createText(value: str) -> Text:
    return Text(value, no_wrap=False, overflow="ELLIPSIS")

def create_table(data_list: list[TableData], color_scheme: ColorScheme) -> DataTable:
    columns = [
        DataColumn((createText("Игрок"))),
        DataColumn(Text("Команда")),
        DataColumn(Text("Амплуа")),
        DataColumn(createText("Минут сыграно")),
        DataColumn(createText("Передач отдано (точных)")),
        DataColumn(createText("Передач не точных")),
        DataColumn(createText("% точности передач")),
        DataColumn(createText("Захватов выполнено")),
        DataColumn(createText("Захватов мимо")),
        DataColumn(createText("% захватов")),
        DataColumn(createText("Раков зачищено")),
        DataColumn(createText("Отборов выполнено")),
        DataColumn(createText("Метров пройдено")),
        DataColumn(createText("Защитников обыграно")),
        DataColumn(createText("Прорывов")),
        DataColumn(createText("Попыток занесено")),
        DataColumn(createText("Реализаций забито")),
        DataColumn(createText("Реализаций пробивалось")),
        DataColumn(createText("% точности реализаций")),
        DataColumn(createText("Штрафных забито")),
        DataColumn(createText("Штрафных пробивалось")),
        DataColumn(createText("% точности штрафных")),
        DataColumn(createText("Дроп-голов забито")),
        DataColumn(createText("Дроп-голов пробивалось")),
        DataColumn(createText("% точности Дроп-голов")),
        DataColumn(createText("Очков набрано")),
        DataColumn(createText("Штрафных получено")),
        DataColumn(createText("Потерь мяча")),
        DataColumn(createText("Желтых карточек")),
        DataColumn(createText("Красных карточек")),
        DataColumn(createText("Рейтинговые баллы")),
    ]
    rows = []
    for d in data_list:
        rows.append(DataRow(cells=[
            DataCell(CupertinoFilledButton(content=Text(d.player.full_name), padding=1, bgcolor=color_scheme.secondary)),
            DataCell(createText(d.team)),
            DataCell(createText(d.role)),
            DataCell(createText(str(d.minutes_played))),
            DataCell(createText(str(d.passes_accurate))),
            DataCell(createText(str(d.passes_inaccurate))),
            DataCell(createText(f"{d.passes_percent:.1f}%")),
            DataCell(createText(str(d.captures_done))),
            DataCell(createText(str(d.captures_missed))),
            DataCell(createText(f"{d.captures_percent:.1f}%")),
            DataCell(createText(str(d.rakov_cleared))),
            DataCell(createText(str(d.tackles_done))),
            DataCell(createText(str(d.meters_covered))),
            DataCell(createText(str(d.defenders_beaten))),
            DataCell(createText(str(d.breakthroughs))),
            DataCell(createText(str(d.attempts_grounded))),
            DataCell(createText(str(d.realizations_scored))),
            DataCell(createText(str(d.realizations_attempted))),
            DataCell(createText(f"{d.realizations_percent:.1f}%")),
            DataCell(createText(str(d.penalties_scored))),
            DataCell(createText(str(d.penalties_attempted))),
            DataCell(createText(f"{d.penalties_percent:.1f}%")),
            DataCell(createText(str(d.dropgoals_scored))),
            DataCell(createText(str(d.dropgoals_attempted))),
            DataCell(createText(f"{d.dropgoals_percent:.1f}%")),
            DataCell(createText(str(d.points_scored))),
            DataCell(createText(str(d.penalties_received))),
            DataCell(createText(str(d.turnovers))),
            DataCell(createText(str(d.yellow_cards))),
            DataCell(createText(str(d.red_cards))),
            DataCell(createText(f"{d.rating:.2f}")),
        ]))

    return DataTable(columns=columns, rows=rows, expand=False,  
        horizontal_lines=BorderSide(1, color_scheme.outline),
        vertical_lines=BorderSide(1, color_scheme.outline), show_bottom_border=True, 
        clip_behavior="hard", border_radius=9, 
        column_spacing=8, divider_thickness=1) 