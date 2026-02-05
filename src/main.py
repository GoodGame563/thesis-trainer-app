import logging

from flet import (
    BottomSheet,
    Card,
    Column,
    Container,
    CupertinoContextMenu,
    CupertinoContextMenuAction,
    FloatingActionButtonLocation,
    Image,
    Page,
    Row,
    Stack,
    icons,
    run,
)

from components import (
    FilterButtomSheet,
    Menu,
    PlayerContainer,
    TeamDialog,
    create_black_overlay,
)
from db_controls import create_db, get_games_statistics
from theme import dark_theme, light_theme
from utils import IconButton, InformationTable

logging.basicConfig(level=logging.INFO)


async def main(page: Page):
    await create_db()

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
    menu = Menu()
    black_overlay = create_black_overlay()

    theme_button = IconButton(icons.Icons.SUNNY, change_theme)

    page.floating_action_button = theme_button
    page.floating_action_button_location = FloatingActionButtonLocation.END_TOP
    player_view = PlayerContainer()
    main_table = InformationTable(
        # []
        await get_games_statistics(),
        # None,
        player_view,
    )
    # page.show_dialog(player_view)
    bs = FilterButtomSheet(main_table.get_columns(), main_table.set_column)
    page.add(
        Container(
            Stack(
                controls=[
                    Card(
                        content=Row(
                            controls=Column(
                                controls=main_table,
                                scroll="ALWAYS",
                            ),
                            scroll="ADAPTIVE",
                            expand=True,
                        ),
                        clip_behavior="none",
                        margin=40,
                        expand=True,
                    ),
                    Container(
                        content=IconButton(
                            icons.Icons.FILTER_LIST,
                            lambda _: page.show_dialog(bs),
                        ),
                        right=0,
                        bottom=0,
                    ),
                    Container(
                        content=IconButton(icons.Icons.MENU, menu.open_menu),
                        top=0,
                        left=0,
                    ),
                    black_overlay,
                    player_view,
                    # filter_view,
                    menu,
                ]
            ),
            expand=True,
            clip_behavior="ANTI_ALIAS_WITH_SAVE_LAYER",
        )
    )

    # player_view.open(12)


if __name__ == "__main__":
    run(main)
