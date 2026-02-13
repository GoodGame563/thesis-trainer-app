import asyncio

from flet import Alignment, MenuBar, MenuStyle

from utils import MenuButton

from .game import GameDialog
from .team import TeamDialog
from .transfer import TransferDialog
from .player import PlayerAddDialog


class Menu(MenuBar):
    def __init__(self):
        super().__init__(
            style=MenuStyle(
                alignment=Alignment.CENTER,
            ),
            controls=[
                MenuButton("Добавить игрока", self.element_open_player),
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

    async def element_open_team(self):
        td = TeamDialog()
        self.page.show_dialog(td)
        await asyncio.sleep(0.3)

    async def element_open_game(self):
        gd = GameDialog()
        self.page.show_dialog(gd)
        await asyncio.sleep(0.1)

    async def element_open_transfer(self):
        td = TransferDialog()
        self.page.show_dialog(td)
        await asyncio.sleep(0.3)

    async def element_open_player(self):
        pd = PlayerAddDialog()
        self.page.show_dialog(pd)
        await asyncio.sleep(0.3)
