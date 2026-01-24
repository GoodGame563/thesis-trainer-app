from flet import (
    Row,
    Container,
    Column,
    Offset,
    Animation,
    AnimationCurve,
    icons,
    Page,
    Text,
    Margin,
    ListView,
    Switch,
    ControlState,
    BoxShadow,
    Colors,
    Dropdown,
)

from theme import AppTheme

from utils import (
    create_basic_text_button,
    create_icon_button,
)

from .overlay import close_overlay, open_overlay


def close_menu(e):
    menu.offset = Offset(-1, 0)
    close_overlay()


def open_menu(e):
    menu.offset = Offset(0, 0)
    open_overlay()


def create_menu() -> Row:
    return menu


menu = Row(
    controls=[
        Container(
            content=Column(
                controls=[
                    create_basic_text_button("Добавить игрока", AppTheme.color_scheme),
                    create_basic_text_button("Добавить матч", AppTheme.color_scheme),
                    create_basic_text_button("Создать команду", AppTheme.color_scheme),
                    create_basic_text_button("Трансфер", AppTheme.color_scheme),
                    create_basic_text_button(
                        "Открыть статистику",
                        AppTheme.color_scheme,
                    ),
                ],
                spacing=10,
                horizontal_alignment="STRETCH",
                width=300,
            ),
            bgcolor=AppTheme.color_scheme.outline,
            padding=20,
        ),
        create_icon_button(icons.Icons.CLOSE, AppTheme.color_scheme, close_menu),
    ],
    vertical_alignment="start",
    spacing=2,
    offset=Offset(-1, 0),
    animate_offset=Animation(300, AnimationCurve.EASE_OUT),
)
