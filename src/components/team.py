from flet import (
    Alignment,
    Animation,
    AnimationCurve,
    Button,
    Card,
    CardVariant,
    Column,
    Container,
    CupertinoTextField,
    Dropdown,
    DropdownOption,
    ListView,
    MainAxisAlignment,
    Margin,
    Offset,
    Row,
    Switch,
    Text,
    TextField,
)

from utils import create_action_text_button, create_basic_text_button

team_view = Card()


def create_team_view() -> Card:
    global team_view
    team_view = Card(
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
                            height=35,
                            # value=value.value,
                            content_padding=0,
                            key="value",
                            label="Название",
                            expand=1,
                            margin=10,
                        ),
                        create_basic_text_button("Загрузить лого"),
                    ]
                ),
                create_action_text_button("Сохранить"),
            ],
            alignment=MainAxisAlignment.SPACE_EVENLY,
        ),
        expand_loose=True,
        align=Alignment.CENTER,
        adaptive=True,
        width=500,
        height=300,
    )
    return team_view
