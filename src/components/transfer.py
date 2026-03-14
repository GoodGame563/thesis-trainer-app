import asyncio
import re
from datetime import datetime

from flet import (
    AlertDialog,
    Card,
    CardVariant,
    Column,
    Container,
    DatePicker,
    MainAxisAlignment,
    Margin,
    Row,
    Text,
    TextField,
)

from db_controls import create_transfer, get_all_players, get_all_teams, get_session
from utils import ActionButton, BasicButton, NormalText, Picker


class TransferDialog(AlertDialog):
    def __init__(self):
        self._date_field = TextField(
            content_padding=2,
            disabled=True,
            value="",
            label="Дата трансфера",
            margin=Margin.only(left=10, right=10, top=5, bottom=0),
            expand=True,
        )
        self.session = get_session()
        self.player_button = ActionButton("Выбрать игрока", self._select_player, 1)
        self.team_button = ActionButton("Выбрать команду", self._select_team, 1)
        super().__init__(
            content=Container(
                content=Column(
                    controls=[
                        Card(
                            content=Text(
                                "Трансфер",
                                no_wrap=False,
                                overflow="ELLIPSIS",
                                expand=True,
                                size=30,
                                text_align="center",
                                margin=10,
                            ),
                            margin=Margin.only(
                                left=10,
                                right=10,
                                top=10,
                                bottom=0,
                            ),
                            clip_behavior=True,
                            variant=CardVariant.OUTLINED,
                        ),
                        Row(
                            controls=[
                                self.player_button,
                                self.team_button,
                            ],
                            expand=1,
                        ),
                        Row(
                            controls=[
                                self._date_field,
                                BasicButton(
                                    "Выбрать дату трансфера", self._select_date
                                ),
                            ],
                            expand=1,
                        ),
                        ActionButton("Загрузить", self._save),
                    ],
                    alignment=MainAxisAlignment.SPACE_EVENLY,
                    expand=True,
                    horizontal_alignment="STRETCH",
                ),
                margin=10,
                width=700,
                height=300,
                expand=True,
            ),
            modal=False,
            on_dismiss=self._dissmiss,
        )

    async def _get_teams(self):
        return [
            NormalText(team.name, team.id) for team in await get_all_teams(self.session)
        ]

    async def _get_players(self):
        return [
            NormalText(player.full_name, player.id)
            for player in await get_all_players(self.session)
        ]

    async def _select_date(self, e):
        async def close_date_picker(d):
            self._date_field.value = d.data.strftime("%d.%m.%Y")
            self._date_field.update()
            await asyncio.sleep(0.2)

        dp = DatePicker(
            cancel_text="Отмена",
            confirm_text="Выбрать",
            error_format_text="Неверный формат даты",
            error_invalid_text="Неверная дата",
            help_text="Выберите дату",
            on_change=close_date_picker,
        )
        self.page.show_dialog(dp)
        await asyncio.sleep(0.2)

    async def _select_player(self, e):
        picker = Picker(e.control)
        self.page.show_dialog(picker)
        await picker.set_data(await self._get_players())

    async def _select_team(self, e):
        picker = Picker(e.control)
        self.page.show_dialog(picker)
        await picker.set_data(await self._get_teams())

    async def _save(self, e):
        e.control.disabled = True
        e.control.update()
        if (
            self.player_button.content.key is None
            or self.team_button.content.key is None
            or re.match(r"\d{2}.\d{2}.\d{4}", self._date_field.value) is None
        ):
            return
        self.open = False
        await create_transfer(
            self.session,
            self.player_button.content.key,
            self.team_button.content.key,
            datetime.strptime(self._date_field.value, "%d.%m.%Y"),
        )

    def _dissmiss(self):
        del self
