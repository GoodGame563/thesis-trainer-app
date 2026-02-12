import asyncio
from flet import (
    Alignment,
    BorderSide,
    Card,
    Colors,
    DataCell,
    DataColumnSortEvent,
    Icons,
    Stack,
)
from flet_datatable2 import DataColumn2, DataColumnSize, DataRow2, DataTable2

from models import ShortTableData, TableData, name_column_table
from theme import light_cs

from .buttons import BasicButton, IconButton
from .player import PlayerContainer
from .text import NormalText


class InformationTable(Card):
    data_table: list[TableData] = []
    index = 0
    step = 15
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

    def __init__(self):
        self.rows = []
        self.columns = []
        for key, value in self.visible_column_table.items():
            self.columns.append(
                DataColumn2(
                    label=NormalText(f"{name_column_table[key]}"),
                    visible=value,
                    key=key,
                    on_sort=self.sort_column,
                    size=DataColumnSize.M,
                )
            )

        self.right_button = IconButton(Icons.ARROW_FORWARD, self.to_right)
        self.left_button = IconButton(Icons.ARROW_BACK, self.to_left)
        self.main_table = DataTable2(
            columns=self.columns,
            rows=self.rows,
            horizontal_lines=BorderSide(1, light_cs.outline),
            vertical_lines=BorderSide(1, light_cs.outline),
            min_width=7000,
            visible_horizontal_scroll_bar=True,
            visible_vertical_scroll_bar=True,
            expand=1,
            heading_row_color=Colors.with_opacity(0.6, light_cs.secondary),
            fixed_columns_color=Colors.with_opacity(0.3, light_cs.outline),
            sort_ascending=True,
            fixed_left_columns=1,
        )
        self.right_button.align = Alignment.CENTER_RIGHT
        self.left_button.align = Alignment.CENTER_LEFT
        super().__init__(
            content=Stack(
                controls=[
                    self.main_table,
                    self.right_button,
                    self.left_button,
                ]
            ),
            clip_behavior="HARD",
        )

    def sort_column(self, e: DataColumnSortEvent):
        if isinstance(self.data_table[0], ShortTableData):
            return
        self.data_table.sort(
            key=lambda element: getattr(element, e.control.key), reverse=not e.ascending
        )
        self.main_table.sort_column_index = e.column_index
        self.main_table.sort_ascending = e.ascending
        self.update_data()

    async def open_user(self, e):
        p_c = PlayerContainer()
        self.page.show_dialog(p_c)
        await p_c.open_user(e.control.key)

    def update_columns(self):
        visible = 0
        for i in range(len(self.columns)):
            value = self.visible_column_table[self.columns[i].key]
            self.columns[i].visible = value
            if value:
                visible += 1
            for row in self.rows:
                row.cells[i].visible = value
        self.main_table.min_width = visible * 218
        self.main_table.update()

    def to_left(self, e):
        self.index -= self.step if self.step - self.index <= 0 else 0
        self.update_data()

    def to_right(self, e):
        self.index += self.step if self.step + self.index <= len(self.data_table) else 0
        self.update_data()

    def manupalate_disabled(self):
        if self.index + self.step >= len(self.data_table):
            self.right_button.disabled = True
            self.right_button.opacity = 0.5
        else:
            self.right_button.disabled = False
            self.right_button.opacity = 1
        if self.index - self.step < 0:
            self.left_button.disabled = True
            self.left_button.opacity = 0.5
        else:
            self.left_button.disabled = False
            self.left_button.opacity = 1

    def get_data_rows(self):
        ROLE_MAPPING = {
            "FIRST_LINE": "Первая линия",
            "SECOND_LINE": "Вторая линия",
            "THIRD_LINE": "Третья линия",
            "SCRUM_HALF": "Полузащитник схватки",
            "FLY_HALF": "Полузащитник веера",
            "CENTER": "Центр",
            "WING": "Крайний",
            "FULLBACK": "Фуллбэк",
            "NOTHING": "Все роли",
        }

        data_rows = []
        for d in self.data_table[self.index : self.index + self.step]:
            cells = []
            for a in self.visible_column_table:
                match a:
                    case "player":
                        button = BasicButton(
                            getattr(d, a).full_name, self.open_user, getattr(d, a).id
                        )
                        button.margin = 5
                        content = button
                    case "date_birth":
                        content = NormalText(d.date_birth.strftime("%d.%m.%Y"))
                    case "team":
                        content = NormalText(d.team)
                    case "role":
                        content = NormalText(ROLE_MAPPING.get(d.role.name, "Увы"))
                    case _:
                        content = NormalText(getattr(d, a))
                cells.append(
                    DataCell(
                        content,
                        visible=self.visible_column_table[a],
                        key=a,
                    )
                )

            data_rows.append(DataRow2(cells=cells))
        return data_rows

    def set_data(self, data_list: list[TableData]):
        self.data_table = data_list
        self.update_data()

    def update_data(self):
        self.rows.clear()
        self.rows.extend(self.get_data_rows())
        self.manupalate_disabled()

    def get_columns(self):
        return self.visible_column_table

    def set_column(self, name_column, value):
        self.visible_column_table[name_column] = value
        self.update_data()

    async def set_columns(self, column_table: dict[str, bool]):
        self.main_table.disabled = True
        self.main_table.update()
        await asyncio.sleep(1)

        for key, value in column_table.items():
            self.visible_column_table[key] = value
        self.update_columns()
        self.main_table.disabled = False
        self.main_table.update()
