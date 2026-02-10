from flet import Animation, AnimationCurve, Column, Container, Offset, Row, icons

from theme import light_theme
from utils import IconButton, MenuButton

from .game import GameDialog
from .overlay import close_overlay, open_overlay
from .team import TeamDialog
from .transfer import TransferDialog


class Menu(Row):
    def __init__(self):
        super().__init__(
            controls=[
                Container(
                    content=Column(
                        controls=[
                            MenuButton("Добавить игрока"),
                            MenuButton(
                                "Добавить матч",
                                self.element_open_game,
                            ),
                            MenuButton("Создать команду", self.element_open_team),
                            MenuButton(
                                "Трансфер",
                                self.element_open_transfer,
                            ),
                            MenuButton(
                                "Открыть статистику",
                            ),
                        ],
                        spacing=10,
                        horizontal_alignment="STRETCH",
                        width=300,
                    ),
                    bgcolor=light_theme.color_scheme.outline,
                    padding=20,
                ),
                IconButton(icons.Icons.CLOSE, self.close_menu),
            ],
            vertical_alignment="start",
            spacing=2,
            offset=Offset(-1, 0),
            animate_offset=Animation(300, AnimationCurve.EASE_IN_OUT),
        )

    def close_menu(self, e):
        self.offset = Offset(-1, 0)
        # close_overlay()

    def close_menu_without_overlay(self):
        self.offset = Offset(-1, 0)

    def open_menu(self, e):
        self.offset = Offset(0, 0)
        # open_overlay()
        self.update()

    def element_open_team(self):
        td = TeamDialog()
        self.page.show_dialog(td)

    async def element_open_game(self):
        gd = GameDialog()
        self.page.show_dialog(gd)

    def element_open_transfer(self):
        td = TransferDialog()
        self.page.show_dialog(td)
