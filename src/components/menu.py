import asyncio

from flet import Alignment, MenuBar, MenuStyle

from db_controls import get_all_games, get_session
from utils import MenuButton, NormalText, Picker

from .game import GameDialog
from .player import PlayerAddDialog
from .team import TeamDialog
from .transfer import TransferDialog


class Menu(MenuBar):
    def __init__(self, set_table):
        self.set_table = set_table
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
                MenuButton("Выбрать матч", self.element_open_match),
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

    async def element_open_match(self, e):
        async def dissmis():
            print(e.control.content.key)
            await self.set_table(e.control.content.key)

        picker = Picker(e.control, dissmis)
        self.page.show_dialog(picker)
        await picker.set_data(
            [NormalText(g.name, g.id) for g in await get_all_games(get_session())]
        )
