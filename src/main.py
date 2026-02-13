import asyncio
import logging

from flet import (
    Column,
    Container,
    CrossAxisAlignment,
    FloatingActionButtonLocation,
    Page,
    Stack,
    icons,
    run,
)

from components import FilterButtomSheet, Menu, PlayerAddDialog
from db_controls import create_db, get_games_statistics
from theme import dark_theme, light_theme
from utils import CustomBSContentBlock, IconButton, InformationTable

logging.basicConfig(level=logging.INFO)


async def main(page: Page):
    await create_db()

    async def change_theme(e):
        page.theme = dark_theme if page.theme == light_theme else light_theme
        page.update()
        theme_button.icon = (
            icons.Icons.SUNNY if page.theme == light_theme else icons.Icons.DARK_MODE
        )
        page.update()

    async def on_dismiss_filter(e):
        column_table = {}
        for s_b in e.control.column_table_container.content.controls:
            column_table[s_b.content.key] = s_b.content.value
        await main_table.set_columns(column_table)

    async def open_filter(e):
        f = FilterButtomSheet(on_dismiss_filter)
        page.show_dialog(f)
        await asyncio.sleep(1)
        await f.set_data(main_table.visible_column_table)

    logging.getLogger("flet_core").setLevel(logging.INFO)
    page.title = "Таблица с фильтром"
    page.padding = 0
    is_dark = {"value": False}
    page.theme_mode = "light"
    page.theme = dark_theme if is_dark["value"] else light_theme

    theme_button = IconButton(icons.Icons.SUNNY, change_theme)
    # page.show_dialog(PlayerAddDialog())

    page.floating_action_button = theme_button
    page.floating_action_button_location = FloatingActionButtonLocation.END_TOP
    main_table = InformationTable()

    page.add(
        Container(
            Stack(
                controls=[
                    Container(
                        content=Column(
                            controls=[
                                Menu(),
                                CustomBSContentBlock(content=main_table, expand=9),
                            ],
                            horizontal_alignment=CrossAxisAlignment.STRETCH,
                        ),
                        margin=20,
                    ),
                    Container(
                        content=IconButton(
                            icons.Icons.FILTER_LIST,
                            open_filter,
                        ),
                        right=0,
                        bottom=0,
                    ),
                ]
            ),
            expand=True,
            clip_behavior="ANTI_ALIAS_WITH_SAVE_LAYER",
        )
    )
    main_table.set_data(await get_games_statistics())


if __name__ == "__main__":
    run(main)
