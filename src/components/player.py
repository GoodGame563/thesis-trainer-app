from flet import (
    Alignment,
    Animation,
    AnimationCurve,
    Border,
    BorderSide,
    Card,
    Column,
    Container,
    CupertinoSlidingSegmentedButton,
    Image,
    ListView,
    Offset,
    Row,
    AlertDialog
)

from utils import BigerTextBlock, BigestText, NormalText

from .overlay import open_overlay


class PlayerContainer(AlertDialog):
    def __init__(self):
        self.name = "Смишня Смишной Смишевич"
        self.date = "01.12.2025"
        self.height = "205"
        self.weight = "90"

        super().__init__(
            content=
                Column(
                    controls=[
                        Row(
                            controls=[
                                Card(
                                    content=Image(
                                        src="not-found.jpg",
                                    ),
                                    expand=1,
                                ),
                                Card(
                                    content=Column(
                                        controls=[
                                            Container(
                                                content=BigestText(self.name),
                                                border=Border(bottom=BorderSide(2.0)),
                                            ),
                                            Row(
                                                controls=[
                                                    Row(
                                                        controls=[
                                                            BigerTextBlock(self.date),
                                                            BigerTextBlock(
                                                                self.height + " см"
                                                            ),
                                                            BigerTextBlock(
                                                                self.weight + "кг"
                                                            ),
                                                        ],
                                                        wrap=False,
                                                        expand=1,
                                                    ),
                                                    ListView(
                                                        controls=[
                                                            BigerTextBlock(self.date),
                                                            BigerTextBlock(self.date),
                                                        ],
                                                        expand=1,
                                                        # height=300
                                                    ),
                                                ],
                                                expand=True
                                            ),
                                        ],
                                        horizontal_alignment="STRETCH",
                                    ),
                                    expand=3,
                                ),
                            ],
                            expand=1,
                        ),
                        Column(
                            controls=[
                                CupertinoSlidingSegmentedButton(
                                    controls=[
                                        NormalText("Рофл"),
                                        NormalText("Рофл"),
                                        NormalText("Рофл"),
                                        NormalText("Рофл"),
                                        NormalText("Рофл"),
                                    ]
                                ),
                                Card(
                                    content=Row(
                                        controls=Column(
                                            controls=[],
                                            # create_table(
                                            #     []
                                            #     # get_games_statistics(),
                                            # ),
                                            scroll="ALWAYS",
                                            # expand=True
                                        ),
                                        scroll="ADAPTIVE",
                                        expand=True,
                                    ),
                                    clip_behavior="none",
                                ),
                            ],
                            expand=2,
                        ),
                    ]
                )
        )

