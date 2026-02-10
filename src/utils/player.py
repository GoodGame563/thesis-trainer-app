from turtle import bgcolor
from types import NoneType

from flet import (
    AlertDialog,
    Alignment,
    Animation,
    AnimationCurve,
    Border,
    BorderSide,
    Card,
    Colors,
    Column,
    Container,
    CupertinoSlidingSegmentedButton,
    Image,
    ListView,
    Offset,
    Row,
)

from db_controls import (
    find_all_teams_by_user_id,
    get_all_games_by_player_team_id,
    get_player_with_roles_and_teams,
)
from models import KpiRole
from utils import (
    BigerTextBlock,
    CustomBSContentBlock,
    CustomSSContentBlock,
    NormalTextBlock,
    SlidingContentBlock,
)

from .shimmer import CustomShimmer
from .short_table import ShortInformationTable
from .text import BigerText, BigestText


class PlayerContainer(AlertDialog):
    def __init__(self):
        self.name_container = Container(
            content=BigestText("Смишня Смишной Смишевич"),
            border=Border(bottom=BorderSide(2.0)),
        )
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
        self.team_name_container = NormalTextBlock("")
        self.game_stat = CustomShimmer(
            SlidingContentBlock(
                text_buttons=("dsadsad", "sadasdas"),
                controls=[Container(), Container()],
                expand=5,
            ),
            expand=5,
        )
        super().__init__(
            content=Column(
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
                                                    controls=self.role_team,
                                                    expand=1,
                                                ),
                                            ],
                                            expand=True,
                                        ),
                                    ],
                                    horizontal_alignment="STRETCH",
                                ),
                                expand=3,
                            ),
                        ],
                        expand=5,
                    ),
                    self.game_stat,
                ]
            )
        )

    async def open_user(self, id):
        pl = await get_player_with_roles_and_teams(id)
        self.name_container.content = BigestText(pl["player"].full_name)
        self.name_container.update()
        self.date_container.content = BigerText(pl["player"].birth_date)
        self.date_container.update()
        self.weight_container.content = BigerText(str(pl["player"].weight) + " кг")
        self.weight_container.update()
        self.height_container.content = BigerText(str(pl["player"].height) + " см")
        self.height_container.update()
        self.role_team.clear()
        self.role_team.extend(
            [
                NormalTextBlock(f"{KpiRole[r_t['role']].value} - {r_t['team']}")
                for r_t in pl["roles_with_team"]
            ]
        )

        self.image_container.content.src = (
            pl["current_team"].path_to_logo if pl["current_team"] else "not-found.jpg"
        )
        self.image_container.update()
        self.team_name_container.content = BigerText(
            pl["current_team"].name if pl["current_team"] else "Нет команды"
        )
        self.team_name_container.update()
        text_buttons = []
        contols = []
        for t in await find_all_teams_by_user_id(id):
            text_buttons.append(t.name)
            i_t = ShortInformationTable()
            i_t.set_data(await get_all_games_by_player_team_id(id, t.id))
            contols.append(i_t)
        self.content.controls[1] = SlidingContentBlock(
            text_buttons=tuple(text_buttons),
            controls=contols,
            expand=5,
        )
        self.update()
