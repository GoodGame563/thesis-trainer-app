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
)

# from models import create_table
from .overlay import open_overlay
from utils import NormalText, BigerTextBlock, BigestText

user_view = Container()

def open_user_view(id):
    global user_view
    user_view.offset = Offset(0,0)
    open_overlay()


def user_information():
    name = "Смишня Смишной Смишевич"
    date = "01.12.2025"
    height = "205"
    weight = "90"
    return Card(
        content=Column(
            controls=[
                Container(
                    content=BigestText(name),
                    border=Border(bottom=BorderSide(2.0)),
                ),
                Row(
                    controls=[
                        Row(
                            controls=[
                                BigerTextBlock(date),
                                BigerTextBlock(height + " см"),
                                BigerTextBlock(weight + "кг"),
                            ],
                            wrap=False,
                            expand=1,
                        ),
                        ListView(controls=[BigerTextBlock(date)], expand=1),
                    ]
                ),
            ],
            horizontal_alignment="STRETCH",
        ),
        expand=3,
    )


def create_user_view():
    global user_view
    user_view = Container(
        content=Card(
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
                            user_information(),
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
        ),
        offset=Offset(-1, 0),
        alignment=Alignment(0, 0),
        margin=50,
        animate_offset=Animation(300, AnimationCurve.EASE_IN_OUT),
    )
    return user_view
