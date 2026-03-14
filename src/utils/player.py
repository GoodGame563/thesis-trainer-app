import asyncio
from datetime import datetime

import aioshutil
from flet import (
    AlertDialog,
    Border,
    BorderSide,
    Card,
    CardVariant,
    Column,
    Container,
    CrossAxisAlignment,
    DatePicker,
    FilePicker,
    FilePickerFileType,
    Icons,
    Image,
    ListView,
    MainAxisAlignment,
    Margin,
    Row,
    Stack,
    Text,
    TextField,
)

from db_controls import (
    find_all_teams_by_user_id,
    get_all_games_by_player_team_id,
    get_player,
    get_players_roles_and_teams,
    get_players_team,
    get_session,
    update_player,
)
from models import KpiRole
from utils import (
    ActionButton,
    BasicButton,
    BigerTextBlock,
    CustomBSContentBlock,
    CustomSSContentBlock,
    IconButton,
    NormalTextBlock,
    SlidingContentBlock,
)

from .shimmer import CustomShimmer
from .short_table import ShortInformationTable
from .text import BigerText, BigestText
from .text_fields import NormalTextField


class PlayerContainer(AlertDialog):
    def __init__(self):
        self.name_container = Container(
            content=BigestText("Смишня Смишной Смишевич"),
            border=Border(bottom=BorderSide(2.0)),
        )
        self.select_id = 0
        self.date_container = BigerTextBlock("dslfksjlk")
        self.height_container = BigerTextBlock("100" + " см")
        self.weight_container = BigerTextBlock("90" + "кг")
        self.role_team = [
            CustomShimmer(
                content=NormalTextBlock("Роль - Команда"),
            )
            for _ in range(8)
        ]
        self.date_container.margin = 3
        self.height_container.margin = 3
        self.weight_container.margin = 3
        self.image_container = CustomSSContentBlock(Image(src="", expand=1))
        self.team_name_container = BigerTextBlock("")
        self.game_stat = CustomShimmer(
            SlidingContentBlock(
                text_buttons=["dsadsad", "sadasdas"],
                controls=[Container(), Container()],
                expand=5,
            ),
            expand=5,
        )
        super().__init__(
            content=Stack(
                controls=[
                    Column(
                        controls=[
                            Row(
                                controls=[
                                    CustomBSContentBlock(
                                        content=Image(
                                            src="not-found.jpg",
                                        ),
                                        expand=1,
                                    ),
                                    CustomBSContentBlock(
                                        content=Column(
                                            controls=[
                                                self.name_container,
                                                Row(
                                                    controls=[
                                                        Column(
                                                            controls=[
                                                                Row(
                                                                    controls=[
                                                                        self.date_container,
                                                                        self.height_container,
                                                                        self.weight_container,
                                                                    ],
                                                                    spacing=0,
                                                                    wrap=False,
                                                                    expand=3,
                                                                ),
                                                                Row(
                                                                    controls=[
                                                                        self.image_container,
                                                                        self.team_name_container,
                                                                    ],
                                                                    expand=4,
                                                                ),
                                                            ],
                                                            expand=1,
                                                        ),
                                                        ListView(
                                                            controls=self.role_team,  # type: ignore
                                                            expand=1,
                                                        ),
                                                    ],
                                                    expand=True,
                                                ),
                                            ],
                                            horizontal_alignment=CrossAxisAlignment.STRETCH,
                                        ),
                                        expand=3,
                                    ),
                                ],
                                expand=5,
                            ),
                            self.game_stat,
                        ]
                    ),
                    IconButton(Icons.CHANGE_CIRCLE, self.open_update_page),
                ]
            )
        )

    async def open_update_page(self):
        p_d = PlayerUpdateDialog(self.select_id)
        self.page.show_dialog(p_d)
        await p_d.set_value()

    async def update_data(self):
        pass

    async def open_user(self, id):
        session = get_session()
        self.select_id = id
        player = await get_player(session, id)
        team = await get_players_team(session, id)
        pl = await get_players_roles_and_teams(session, id)
        self.name_container.content = BigestText(player.full_name)
        self.name_container.update()
        self.date_container.change_text(player.birth_date.strftime("%d.%m.%Y"))
        self.weight_container.change_text(f"{player.weight} кг")
        self.height_container.change_text(f"{player.height} см")
        self.team_name_container.change_text(team.name if team else "Нет команды")

        self.role_team.clear()
        self.role_team.extend(
            [NormalTextBlock(f"{KpiRole[r_t[0]].value} - {r_t[1]}") for r_t in pl]
        )

        self.image_container.content.src = (
            team.path_to_logo if team else "not-found.jpg"
        )
        self.image_container.update()
        # self.team_name_container.content = BigerText(

        # )
        # self.team_name_container.update()
        text_buttons = []
        contols = []
        for t in await find_all_teams_by_user_id(session, id):
            text_buttons.append(t.name)
            i_t = ShortInformationTable()
            i_t.set_data(await get_all_games_by_player_team_id(session, id, t.id))
            contols.append(i_t)
            self.content.controls[0].controls[1] = SlidingContentBlock(
                text_buttons=text_buttons,
                controls=contols,
                expand=5,
            )
        # self.update()


class PlayerUpdateDialog(AlertDialog):
    def __init__(self, player_id: int):
        self.player_id = player_id
        self.session = get_session()

        self.full_name_field = NormalTextField(
            "Полное ФИО",
        )
        self.height_field = NormalTextField(
            "Рост (см)",
        )
        self.weight_field = NormalTextField(
            "Вес (кг)",
        )
        self.date_birth_field = NormalTextField(
            disabled=True,
            label="Дата рождения",
        )

        super().__init__(
            content=Container(
                content=Column(
                    controls=[
                        Card(
                            content=Text(
                                "Обновить игрока",
                                no_wrap=False,
                                overflow="ELLIPSIS",  # type: ignore
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
                                self.full_name_field,
                            ],
                            expand=1,
                        ),
                        Row(
                            controls=[
                                self.height_field,
                                self.weight_field,
                            ],
                            expand=1,
                        ),
                        Row(
                            controls=[
                                self.date_birth_field,
                                BasicButton(
                                    "Выбрать дату рождения", self.select_date_birth
                                ),
                            ],
                            expand=1,
                        ),
                        ActionButton("Сохранить", self.save),
                    ],
                    expand=True,
                    horizontal_alignment="STRETCH",
                ),
                margin=10,
                width=700,
                height=400,
                expand=True,
            ),
        )

    async def set_value(self):
        player = await get_player(self.session, self.player_id)
        self.full_name_field.value = player.full_name
        self.height_field.value = str(player.height)
        self.weight_field.value = str(player.weight)
        self.date_birth_field.value = player.birth_date.isoformat()

    async def on_mount(self):
        session = get_session()
        player = await get_player(session, self.player_id)
        self.full_name_field.value = player.full_name
        self.height_field.value = str(player.height)
        self.weight_field.value = str(player.weight)
        self.date_birth_field.value = player.birth_date.strftime("%d.%m.%Y")
        self.update()

    async def select_date_birth(self, e):
        async def close_date_picker(d):
            self.date_birth_field.value = d.data.strftime("%d.%m.%Y")
            self.date_birth_field.update()
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

    async def save(self):
        # if (
        #     not self.full_name_field.value
        #     or not self.height_field.value
        #     or not self.weight_field.value
        #     or not self.date_birth_field.value
        # ):
        #     return

        # try:
        height = int(self.height_field.value)
        weight = int(self.weight_field.value)
        date_birth = datetime.strptime(self.date_birth_field.value, "%Y-%m-%d").date()
        # except ValueError:
        #     return

        self.open = False
        await asyncio.sleep(0.2)
        await update_player(
            self.session,
            self.player_id,
            full_name=self.full_name_field.value,
            height=height,
            weight=weight,
            date_birth=date_birth,
        )
