from flet import BorderSide, DataCell, DataColumn, DataRow, DataTable

from models import TableData, name_column_table
from theme import light_cs

from .buttons import BasicButton
from .text import NormalText


class InformationTable(DataTable):
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

    def __init__(self, data_list: list[TableData], open_user_view):
        rows = []
        for d in data_list:
            cells = []
            for a in self.visible_column_table:
                match a:
                    case "player":
                        button = BasicButton(getattr(d, a).full_name, open_user_view)
                        button.margin = 5
                        content = button
                    case "date_birth":
                        content = NormalText(d.player.birth_date)
                    case "team":
                        content = NormalText(d.player.team.name)
                    case _:
                        content = NormalText(getattr(d, a))
                cells.append(
                    DataCell(
                        content,
                        visible=self.visible_column_table[a],
                        key=a,
                    )
                )
            rows.append(DataRow(cells=cells))
        super().__init__(
            columns=[
                DataColumn(
                    NormalText(f"{name_column_table[key]}"), visible=value, key=key
                )
                for key, value in self.visible_column_table.items()
            ],
            rows=rows,
            horizontal_lines=BorderSide(1, light_cs.outline),
            vertical_lines=BorderSide(1, light_cs.outline),
            clip_behavior="hard",
            border_radius=9,
            divider_thickness=1,
        )

    def update(self):
        for i in range(len(self.columns)):
            value = self.visible_column_table[self.columns[i].key]
            self.columns[i].visible = value
            for row in self.rows:
                row.cells[i].visible = value
        super().update()

    def get_columns(self):
        return self.visible_column_table

    def set_column(self, name_column, value):
        self.visible_column_table[name_column] = value
        self.update()
