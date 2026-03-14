import asyncio

from flet import (
    AlertDialog,
    Card,
    CardVariant,
    ClipBehavior,
    Column,
    Container,
    CrossAxisAlignment,
    FilePicker,
    FilePickerFileType,
    MainAxisAlignment,
    Margin,
    Row,
    Text,
    TextAlign,
    TextField,
)

from db_controls import add_game, add_stat, get_all_teams, get_session
from exsel_reader import parse_excel_to_stats
from models import Team
from utils import ActionButton, BasicButton, NormalText, Picker


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
        self.session = get_session()
        super().__init__(
            content=Container(
                content=Column(
                    controls=[
                        Card(
                            content=Text(
                                "Добавить матч",
                                no_wrap=False,
                                overflow="ELLIPSIS",  # type: ignore
                                expand=True,
                                size=30,
                                text_align=TextAlign.CENTER,
                                margin=10,
                            ),
                            margin=Margin.only(
                                left=10,
                                right=10,
                                top=10,
                                bottom=0,
                            ),
                            clip_behavior=ClipBehavior.ANTI_ALIAS,
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
                    horizontal_alignment=CrossAxisAlignment.STRETCH,
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
        self.path_file_field.value = (
            file[0].path if isinstance(file[0].path, str) else ""
        )
        self.path_file_field.update()
        await asyncio.sleep(0.1)

    async def _get_teams(self):
        teams = await get_all_teams(self.session)
        return [NormalText(team.name, team.id) for team in teams]

    async def select_team(self, e):
        picker = Picker(e.control)
        self.page.show_dialog(picker)
        await picker.set_data(await self._get_teams())

    async def save(self):
        self.open = False
        if (
            isinstance(self.f_team_button.content, str)
            or self.f_team_button.content is None
            or isinstance(self.s_team_button.content, str)
            or self.s_team_button.content is None
        ):
            return
        if not isinstance(self.f_team_button.content, NormalText):
            return
        team_1_key = self.f_team_button.content.key
        team_2_key = self.s_team_button.content.key

        if team_1_key is None or team_2_key is None:
            return

        new_id = await add_game(
            self.session,
            Team(team_1_key, self.f_team_button.content.value, ""),
            Team(self.s_team_button.content.key, self.s_team_button.content.value, ""),
        )
        for s in parse_excel_to_stats(self.path_file_field.value, new_id):
            if int(s.team) == 1:
                s.team = self.f_team_button.content.key
            elif int(s.team) == 2:
                s.team = self.s_team_button.content.key
            await add_stat(self.session, s)

    def dissmiss(self):
        del self
