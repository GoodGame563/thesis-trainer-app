import logging

from flet import (
    Animation,
    Card,
    Colors,
    Column,
    Container,
    FloatingActionButton,
    FloatingActionButtonLocation,
    Offset,
    Page,
    Row,
    Stack,
    icons,
    run,
)

from components import (
    create_black_overlay,
    create_filter_view,
    create_menu,
    open_filter_view,
    open_menu,
)
from db_controls import create_db, get_games_statistics
from models import create_empty, create_table
from theme import dark_theme, light_theme
from utils import create_icon_button

logging.basicConfig(level=logging.INFO)

create_db()


async def main(page: Page):

    async def change_theme(e):
        page.theme = dark_theme if page.theme == light_theme else light_theme
        theme_button.icon = (
            icons.Icons.SUNNY if page.theme == light_theme else icons.Icons.DARK_MODE
        )
        page.update()

    logging.getLogger("flet_core").setLevel(logging.INFO)
    page.title = "Таблица с фильтром"
    page.padding = 0
    is_dark = {"value": False}
    page.theme_mode = "light"
    page.theme = dark_theme if is_dark["value"] else light_theme
    menu = create_menu()
    black_overlay = create_black_overlay()
    # print(data)

    theme_button = create_icon_button(icons.Icons.SUNNY, change_theme)

    page.floating_action_button = theme_button
    page.floating_action_button_location = FloatingActionButtonLocation.END_TOP

    filter_view = create_filter_view()

    page.add(
        Container(
            Stack(
                controls=[
                    Card(
                        content=Row(
                            controls=Column(
                                controls=create_table(
                                    # []
                                    get_games_statistics(),
                                ),
                                scroll="ALWAYS",
                                # expand=True
                            ),
                            scroll="ADAPTIVE",
                            expand=True,
                        ),
                        clip_behavior="none",
                        margin=40,
                        expand=True,
                    ),
                    Container(
                        content=create_icon_button(
                            icons.Icons.FILTER_LIST,
                            open_filter_view,
                        ),
                        right=0,
                        bottom=0,
                    ),
                    Container(
                        content=create_icon_button(icons.Icons.MENU, open_menu),
                        top=0,
                        left=0,
                    ),
                    black_overlay,
                    filter_view,
                    menu,
                ]
            ),
            expand=True,
            clip_behavior="ANTI_ALIAS_WITH_SAVE_LAYER",
        )
    )


if __name__ == "__main__":
    run(main)
