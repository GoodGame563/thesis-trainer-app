from flet import Animation, AnimationCurve, Column, Container, Offset, Row, icons

from theme import light_theme
from utils import create_basic_text_button, create_icon_button

from .overlay import close_overlay, open_overlay

from .team import open_team_view


def close_menu(e):
    menu.offset = Offset(-1, 0)
    close_overlay()

def close_menu_without_overlay():
    menu.offset = Offset(-1, 0)

def open_menu(e):
    menu.offset = Offset(0, 0)
    open_overlay()

def element_open_team():
    close_menu_without_overlay()
    open_team_view()


def create_menu() -> Row:
    global menu
    menu = Row(
        controls=[
            Container(
                content=Column(
                    controls=[
                        create_basic_text_button("Добавить игрока"),
                        create_basic_text_button(
                            "Добавить матч",
                        ),
                        create_basic_text_button(
                            "Создать команду",
                            element_open_team
                        ),
                        create_basic_text_button(
                            "Трансфер",
                        ),
                        create_basic_text_button(
                            "Открыть статистику",
                        ),
                    ],
                    spacing=10,
                    horizontal_alignment="STRETCH",
                    width=300,
                ),
                bgcolor=light_theme.color_scheme.outline,
                padding=20,
            ),
            create_icon_button(icons.Icons.CLOSE, close_menu),
        ],
        vertical_alignment="start",
        spacing=2,
        offset=Offset(-1, 0),
        animate_offset=Animation(300, AnimationCurve.EASE_IN_OUT),
    )
    return menu


menu = Row()
