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

from db_controls import get_all_players, get_all_teams, get_latest_transfer
from utils import ActionButton, BasicButton, NormalText

from .overlay import close_overlay, open_overlay


class TransferDialog(AlertDialog):
    def __init__(self):
        self.teams = []
        self.path_file_field = TextField(
            content_padding=2,
            disabled=True,
            value="",
            label="Путь",
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
                                ActionButton("Выбрать игрока", self.select_player, 1),
                                ActionButton("Выбрать команду", self.select_team, 1),
                            ],
                            expand=1,
                        ),
                        Row(
                            controls=[
                                self.path_file_field,
                                BasicButton("Загрузить игру"),
                            ],
                            expand=1,
                        ),
                        ActionButton("Загрузить", self.save),
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
            on_dismiss=self.dissmiss,
        )

    async def _set_teams(self):
        if len(self.teams) > 0:
            return
        teams = await get_all_teams()
        self.teams.clear()
        self.teams.extend([NormalText(team.name) for team in teams])

    async def select_player(self, e):
        await self._set_teams()

        def set_button(d):
            e.control.content = self.teams[d.data]
            e.control.key = d.data

        picker = CupertinoPicker(
            controls=self.teams,
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

    async def select_team(self, e):
        await self._set_teams()

        def set_button(d):
            e.control.content = self.teams[d.data]
            e.control.key = d.data

        picker = CupertinoPicker(
            controls=self.teams,
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

    def save(self):
        self.open = False

    def dissmiss(self):
        del self
