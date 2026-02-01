from flet import (
    Alignment,
    Animation,
    AnimationCurve,
    Border,
    BorderSide,
    Button,
    Card,
    CardVariant,
    Colors,
    Column,
    Container,
    CupertinoSlidingSegmentedButton,
    CupertinoTextField,
    Dropdown,
    DropdownOption,
    Image,
    ListView,
    MainAxisAlignment,
    Margin,
    Offset,
    ResponsiveRow,
    Row,
    Switch,
    Text,
    TextField,
    View,
)

from models import create_table
from utils import (
    create_action_text_button,
    create_basic_text,
    create_basic_text_button,
    create_biger_text_block,
    create_bigest_text,
)

from .overlay import close_overlay, open_overlay

user_view = Container()


def user_information():
    name = "Смишня Смишной Смишевич"
    date = "01.12.2025"
    height = "205"
    weight = "90"
    return Card(
        content=Column(
            controls=[
                Container(
                    content=create_bigest_text(name),
                    border=Border(bottom=BorderSide(2.0)),
                ),
                Row(
                    controls=[
                        Row(
                            controls=[
                                create_biger_text_block(date),
                                create_biger_text_block(height + " см"),
                                create_biger_text_block(weight + "кг"),
                            ],
                            wrap=False,
                            expand=1,
                        ),
                        ListView(controls=[create_biger_text_block(date)], expand=1),
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
                                    src=f"not-found.jpg",
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
                                    create_basic_text("Рофл"),
                                    create_basic_text("Рофл"),
                                    create_basic_text("Рофл"),
                                    create_basic_text("Рофл"),
                                    create_basic_text("Рофл"),
                                ]
                            ),
                            Card(
                                content=Row(
                                    controls=Column(
                                        controls=create_table(
                                            []
                                            # get_games_statistics(),
                                        ),
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
        offset=Offset(0, 0),
        alignment=Alignment(0, 0),
        margin=50,
        animate_offset=Animation(300, AnimationCurve.EASE_IN_OUT),
    )
    return user_view
