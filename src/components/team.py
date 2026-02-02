from flet import (
    Alignment,
    Animation,
    AnimationCurve,
    Card,
    CardVariant,
    Column,
    Container,
    MainAxisAlignment,
    Margin,
    Offset,
    Row,
    Text,
    TextField,
)

from utils import ActionButton, BasicButton

from .overlay import close_overlay, open_overlay

team_view = Card()


def open_team_view():
    team_view.offset = Offset(0, 0)
    open_overlay()


def close_team_view():
    team_view.offset = Offset(0, 1)
    close_overlay()


def create_team_view() -> Card:
    global team_view
    team_view = Container(
        content=Card(
            content=Container(
                content=Column(
                    controls=[
                        Card(
                            content=Text(
                                "Создать команду",
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
                                TextField(
                                    content_padding=2,
                                    # key="value",
                                    label="Название",
                                    margin=Margin.only(
                                        left=10, right=10, top=5, bottom=0
                                    ),
                                    expand=True,
                                ),
                                BasicButton("Загрузить лого"),
                            ]
                        ),
                        ActionButton("Сохранить", close_team_view),
                    ],
                    alignment=MainAxisAlignment.SPACE_EVENLY,
                    expand=True,
                    horizontal_alignment="STRETCH",
                ),
                margin=20,
            ),
            width=600,
            height=300,
            expand=False,
        ),
        offset=Offset(0, 1),
        alignment=Alignment(0, 0),
        animate_offset=Animation(300, AnimationCurve.EASE_IN_OUT),
    )
    return team_view
