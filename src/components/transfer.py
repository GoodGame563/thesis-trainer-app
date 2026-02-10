import re
from datetime import datetime

from flet import (
    AlertDialog,
    Alignment,
    Animation,
    AnimationCurve,
    Card,
    CardVariant,
    Column,
    Container,
    CupertinoBottomSheet,
    CupertinoPicker,
    DatePicker,
    FilePicker,
    FilePickerFileType,
    ListView,
    MainAxisAlignment,
    Margin,
    Offset,
    Row,
    Text,
    TextField,
)

from db_controls import (
    create_transfer,
    get_all_players,
    get_all_teams,
    get_latest_transfer,
)
from utils import ActionButton, BasicButton, NormalText

from .overlay import close_overlay, open_overlay


class TransferDialog(AlertDialog):
    def __init__(self):
        self._player_id = None
        self._team_id = None
        self._teams = []
        self._players = []
        self._date_field = TextField(
            content_padding=2,
            disabled=True,
            value="",
            label="Дата трансфера",
            margin=Margin.only(left=10, right=10, top=5, bottom=0),
            expand=True,
        )

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
                                ActionButton("Выбрать игрока", self._select_player, 1),
                                ActionButton("Выбрать команду", self._select_team, 1),
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

    async def _set_teams(self):
        if len(self._teams) > 0:
            return
        teams = await get_all_teams()
        self._teams.clear()
        self._teams.extend([NormalText(team.name, team.id) for team in teams])

    async def _set_players(self):
        if len(self._players) > 0:
            return
        players = await get_all_players()
        self._players.clear()
        self._players.extend(
            [NormalText(player.full_name, player.id) for player in players]
        )

    def _select_date(self, e):
        def close_date_picker(d):
            if d.name == "dismiss":
                return
            self._date_field.value = d.data.strftime("%d.%m.%Y")
            self._date_field.update()

        dp = DatePicker(
            cancel_text="Отмена",
            confirm_text="Выбрать",
            error_format_text="Неверный формат даты",
            error_invalid_text="Неверная дата",
            help_text="Выберите дату",
            on_dismiss=close_date_picker,
            on_change=close_date_picker,
        )
        self.page.show_dialog(dp)

    async def _select_player(self, e):
        await self._set_players()

        def set_button(d):
            e.control.content = self._players[d.control.selected_index].value
            e.control.key = self._players[d.control.selected_index].key
            self._player_id = self._players[d.control.selected_index].key

        picker = CupertinoPicker(
            controls=self._players,
            expand=1,
            selected_index=5,
            magnification=1.22,
            squeeze=1.2,
            use_magnifier=True,
            on_change=set_button,
        )
        bs = CupertinoBottomSheet(
            picker,
            height=216,
        )

        self.page.show_dialog(bs)

    async def _select_team(self, e):
        await self._set_teams()

        def set_button(d):
            e.control.content = self._teams[d.control.selected_index].value
            e.control.key = self._teams[d.control.selected_index].key
            self._team_id = self._teams[d.control.selected_index].key

        picker = CupertinoPicker(
            controls=self._teams,
            expand=1,
            selected_index=5,
            magnification=1.22,
            squeeze=1.2,
            use_magnifier=True,
            on_change=set_button,
        )
        bs = CupertinoBottomSheet(
            picker,
            height=216,
        )

        self.page.show_dialog(bs)

    async def _save(self):
        print(
            await create_transfer(
                self._player_id,
                self._team_id,
                datetime.strptime(self._date_field.value, "%d.%m.%Y"),
            )
        )
        self.open = False

    def _dissmiss(self):
        del self
