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
    ThemeMode,
    ClipBehavior,
)

from components import FilterButtomSheet, Menu
from models import KpiRole, anything_changed, calculate_kpi
from db_controls import (
    create_db,
    get_games_statistics,
    get_session,
    set_engine,
    get_all_games,
)
from theme import dark_theme, light_theme
from utils import CustomBSContentBlock, IconButton, InformationTable

logging.basicConfig(level=logging.INFO)


async def main(page: Page):

    engine = await create_db()
    set_engine(engine)
    session = get_session()

    async def change_theme(e):
        page.theme = dark_theme if page.theme == light_theme else light_theme
        theme_button.icon = (
            icons.Icons.SUNNY if page.theme == light_theme else icons.Icons.DARK_MODE
        )
        page.update()

    async def on_dismiss_filter(e):
        role_selected = e.control.switch_role_select.content.value
        column_table = {}
        for s_b in e.control.column_table_container.content.controls:
            column_table[s_b.content.key] = s_b.content.value
        if anything_changed():
            get_stats = await get_games_statistics(
                session, game_id=main_table.index_game
            )
            new_table_data = []
            for stat in get_stats:
                new_table_data.append(await calculate_kpi(role_selected, stat))
            await asyncio.gather(
                main_table.set_columns(column_table),
                main_table.set_data(new_table_data),
            )
        else:
            await main_table.set_columns(column_table)

        await main_table.set_columns(column_table)
        await main_table.set_data(new_table_data)

    async def open_filter(e):
        f = FilterButtomSheet(on_dismiss_filter)
        page.show_dialog(f)
        await asyncio.sleep(0.4)
        await f.set_data(main_table.visible_column_table)

    async def set_table(id):
        await main_table.set_data(await get_games_statistics(session, game_id=id))
        main_table.set_game_index(id)

    logging.getLogger("flet_core").setLevel(logging.INFO)
    page.title = "Таблица с фильтром"
    page.padding = 0
    is_dark = {"value": False}
    page.theme_mode = ThemeMode.LIGHT
    page.theme = dark_theme if is_dark["value"] else light_theme

    theme_button = IconButton(icons.Icons.SUNNY, change_theme)

    page.floating_action_button = theme_button
    page.floating_action_button_location = FloatingActionButtonLocation.END_TOP
    main_table = InformationTable(8)

    page.add(
        Container(
            Stack(
                controls=[
                    Container(
                        content=Column(
                            controls=[
                                Menu(set_table),
                                main_table,
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
            clip_behavior=ClipBehavior.ANTI_ALIAS_WITH_SAVE_LAYER,
        )
    )


if __name__ == "__main__":
    run(main)
