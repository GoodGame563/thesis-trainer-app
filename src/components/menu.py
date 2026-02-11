from flet import (
    Animation,
    AnimationCurve,
    Column,
    Container,
    Offset,
    Row,
    icons,
    MenuBar,
    Alignment,
    MenuStyle
)

from theme import light_theme
from utils import IconButton, MenuButton

from .game import GameDialog
from .overlay import close_overlay, open_overlay
from .team import TeamDialog
from .transfer import TransferDialog


class Menu(MenuBar):
    def __init__(self):
        super().__init__(
             style=MenuStyle(
                alignment=Alignment.CENTER,
            ),
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
            ],
            expand=1,
        )

    def element_open_team(self):
        td = TeamDialog()
        self.page.show_dialog(td)

    async def element_open_game(self):
        gd = GameDialog()
        self.page.show_dialog(gd)

    def element_open_transfer(self):
        td = TransferDialog()
        self.page.show_dialog(td)
