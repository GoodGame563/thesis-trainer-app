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
    AlertDialog,
)

from utils import ActionButton, BasicButton

from .overlay import close_overlay, open_overlay


class TeamDialog(AlertDialog):
    def __init__(self):
        super().__init__(
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
                        ActionButton(
                            "Сохранить",
                        ),
                    ],
                    alignment=MainAxisAlignment.SPACE_EVENLY,
                    expand=True,
                    horizontal_alignment="STRETCH",
                ),
                margin=20,
                width=600,
                height=300,
                expand=False,
            ),
        )
        # animate_offset=Animation(300, AnimationCurve.EASE_IN_OUT),
