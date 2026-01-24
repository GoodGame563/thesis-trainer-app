from flet import (
    ColorScheme,
    Page,
    run,
    icons,
    Column,
    Container,
    BoxShadow,
    Offset,
    Animation,
    Row,
    Stack,
    Colors,
    Margin,
    Switch,
    ControlState,
    PopupMenuButton,
    PopupMenuItem,
    PopupMenuPosition,
    TextField,
    Dropdown,
    DropdownOption,
)


import logging
from theme import light_theme, dark_theme, base_shadow, AppTheme
from components import (
    create_menu,
    create_filter_view,
    create_black_overlay,
    open_menu,
    open_filter_view,
)
from models import create_table, create_empty
from utils import (
    create_icon_button,
    create_basic_text,
    create_action_text_button,
    create_basic_text_button,
)

logging.basicConfig(level=logging.INFO)


async def main(page: Page):
    logging.getLogger("flet_core").setLevel(logging.INFO)
    page.title = "Таблица с фильтром"
    page.padding = 0
    is_dark = {"value": False}
    page.theme = dark_theme if is_dark["value"] else light_theme
    global AppTheme
    AppTheme = page.theme

    menu = create_menu()
    black_overlay = create_black_overlay()
    table = create_table(
        [create_empty(), create_empty(), create_empty()],
    )
    filter_view = create_filter_view()

    page.add(
        Container(
            Stack(
                controls=[
                    Container(
                        padding=0,
                        content=Column(
                            controls=Row(controls=table, scroll="AUTO", expand=True),
                            scroll="AUTO",
                            expand=True,
                        ),
                        bgcolor=page.theme.color_scheme.surface,
                        clip_behavior="none",
                        animate=Animation(250),
                        border_radius=16,
                        margin=40,
                        shadow=[base_shadow],
                        expand=True,
                    ),
                    Container(
                        content=create_icon_button(
                            icons.Icons.FILTER_LIST,
                            page.theme.color_scheme,
                            open_filter_view,
                        ),
                        right=0,
                        bottom=0,
                    ),
                    Container(
                        content=create_icon_button(
                            icons.Icons.MENU, page.theme.color_scheme, open_menu
                        ),
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
