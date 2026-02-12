import asyncio
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

from db_controls import get_all_teams
from utils import ActionButton, BasicButton, NormalText, CustomShimmer, Picker

from .overlay import close_overlay, open_overlay


class GameDialog(AlertDialog):
    def __init__(self):
        self.path_file_field = TextField(
            content_padding=2,
            disabled=True,
            value="",
            label="Путь",
            margin=Margin.only(left=10, right=10, top=5, bottom=0),
            expand=True,
        )
        self.f_team_button = ActionButton("Выбрать команду", self.select_team, 1)
        self.s_team_button = ActionButton("Выбрать команду", self.select_team, 1)

        super().__init__(
            content=Container(
                content=Column(
                    controls=[
                        Card(
                            content=Text(
                                "Добавить матч",
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
                                self.f_team_button,
                                self.s_team_button,
                            ],
                            expand=1,
                        ),
                        Row(
                            controls=[
                                self.path_file_field,
                                BasicButton("Загрузить игру", self.open_select_window),
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

    async def open_select_window(self):
        file = await FilePicker().pick_files(
            file_type=FilePickerFileType.CUSTOM,
            allow_multiple=False,
            allowed_extensions=["xlsx", "xls"],
        )
        self.path_file_field.value = file[0].path
        self.path_file_field.update()
        await asyncio.sleep(0.1)

    async def _get_teams(self):
        teams = await get_all_teams()
        return [NormalText(team.name, team.id) for team in teams]

    async def select_team(self, e):
        picker = Picker(e.control)
        self.page.show_dialog(picker)
        await picker.set_data(await self._get_teams())


    def save(self):
        self.open = False

    def dissmiss(self):
        del self
