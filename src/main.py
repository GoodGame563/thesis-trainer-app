from flet import (
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
    DropdownOption
)

import logging
from theme import light_theme, dark_theme
from components import create_menu, create_filter_view, create_black_overlay
from structs import СomparisonType, Role
from table import (
    create_table,
    visible_column_table,
    name_column_table,
    update_table,
    create_empty,
    positive_indicators,
    negative_indicators
)
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
   

    base_shadow = BoxShadow(
        color=Colors.with_opacity(
            0.5,
            page.theme.color_scheme.shadow,
        ),
        offset=Offset(0, 0),
        blur_radius=12.3,
        blur_style="OUTER",
    )
    small_shadow = BoxShadow(
        color=Colors.with_opacity(
            0.5,
            page.theme.color_scheme.shadow,
        ),
        offset=Offset(0, 0),
        blur_radius=6,
        blur_style="OUTER",
    )

    def open_menu(e):
        logging.info("Menu opened")
        menu.offset = Offset(0, 0)
        black_overlay.offset = Offset(0, 0)
        black_overlay.opacity = 1.0
        # page.update()

    def chage_content_button(e):
        match e.control.key:
            case СomparisonType.EQUALLY:
                e.control.key = СomparisonType.LESS
            case СomparisonType.LESS:
                e.control.key = СomparisonType.EQUALLY_MORE
            case СomparisonType.MORE:
                e.control.key = СomparisonType.EQUALLY_MORE
            case СomparisonType.EQUALLY_MORE:
                e.control.key = СomparisonType.EQUALLY_LESS
            case СomparisonType.EQUALLY_LESS:
                e.control.key = СomparisonType.EQUALLY
        e.control.content.value = e.control.key.value

    def close_menu(e):
        logging.info("Menu closed")
        black_overlay.offset = Offset(-1, 0)
        black_overlay.opacity = 0.0
        menu.offset = Offset(-1, 0)
        # page.update()

    def open_filter_view(e):
        filter_view.offset = Offset(0, 0)
        black_overlay.offset = Offset(0, 0)
        black_overlay.opacity = 1.0
        # page.update()

    def safe_button(e):
        for c in column_table:
            visible_column_table[c.content.key] = c.content.value
        update_table(table)
        filter_view.offset = Offset(0, 1)
        black_overlay.offset = Offset(-1, 0)
        black_overlay.opacity = 0.0
        table.update()
        # page.update()

    def change_switch(e):
        e.control.data.disabled = not e.control.value
    
    def get_positive_table():
        positive_table = []
        for key, value in positive_indicators.items():
            button = create_basic_text_button(
                "=", page.theme.color_scheme, chage_content_button
            )
            button.style.padding = 0
            button.margin = 5
            button.width = 35
            button.height = 35
            button.key = СomparisonType.EQUALLY
            field = TextField(
                height=35,
                content_padding=0,
                expand=1,
                margin=Margin.only(right=5),
            )
            switch = Switch(
                label=name_column_table[key],
                key=key,
                value=False if value == None else True,
                thumb_color={
                    ControlState.SELECTED: page.theme.color_scheme.tertiary,
                    ControlState.DISABLED: page.theme.color_scheme.primary,
                },
                data=field,
                track_color=page.theme.color_scheme.primary,
                on_change=change_switch,
            )
            field.disabled = not switch.value
            positive_table.append(
                Container(
                    content=Row(controls=[switch, button, field]),
                    bgcolor=page.theme.color_scheme.surface,
                    margin=Margin.only(
                        left=10,
                        right=10,
                        top=8,
                        bottom=0,
                    ),
                    border_radius=8,
                    shadow=[small_shadow],
                )
            )
        return positive_table
    
    def get_negative_table():
        negative_table = []
        for key, value in negative_indicators.items():
            button = create_basic_text_button(
                "=", page.theme.color_scheme, chage_content_button
            )
            button.style.padding = 0
            button.margin = 5
            button.width = 35
            button.height = 35
            button.key = СomparisonType.EQUALLY
            field = TextField(
                height=35,
                content_padding=0,
                expand=1,
                margin=Margin.only(right=5),
            )
            switch = Switch(
                label=name_column_table[key],
                key=key,
                value=False if value == None else True,
                thumb_color={
                    ControlState.SELECTED: page.theme.color_scheme.error,
                    ControlState.DISABLED: page.theme.color_scheme.primary,
                },
                # data=field,
                track_color=page.theme.color_scheme.primary,
                # on_change=change_switch,
            )
            # field.disabled = not switch.value
            negative_table.append(
                Container(
                    content=Row(controls=[switch, button, field]),
                    bgcolor=page.theme.color_scheme.surface,
                    margin=Margin.only(
                        left=10,
                        right=10,
                        top=8,
                        bottom=0,
                    ),
                    border_radius=8,
                    shadow=[small_shadow],
                )
            )
        return negative_table
        

    def get_option():
        options = []
        for role in Role:
            key = role.value
            if role.name == 'NOTHING':
                key = 'Все роли'
            options.append(
                DropdownOption(
                    key=key,
                    data=[get_positive_table(), get_negative_table()]
                )

            )
        return options

    column_table = []
    for key, value in visible_column_table.items():
        column_table.append(
            Container(
                content=Switch(
                    label=name_column_table[key],
                    key=key,
                    value=value,
                    thumb_color={
                        ControlState.SELECTED: page.theme.color_scheme.secondary,
                        ControlState.DISABLED: page.theme.color_scheme.primary,
                    },
                    track_color=page.theme.color_scheme.primary,
                ),
                bgcolor=page.theme.color_scheme.surface,
                margin=Margin.only(
                    left=10,
                    right=10,
                    top=8,
                    bottom=0,
                ),
                border_radius=8,
                shadow=[small_shadow],
            )
        )

    dropdown = Dropdown(
        value=0,
        options=get_option(),
        bgcolor=page.theme.color_scheme.surface
    )

    

    table = create_table(
        [create_empty(), create_empty(), create_empty()],
        page.theme.color_scheme,
        visible_column_table,
    )

    menu = create_menu(page, close_menu)
    # filter_view = Container(
    #     offset=Offset(1,1)

    # )
    filter_view = create_filter_view(
        page, base_shadow, small_shadow, column_table, dropdown, safe_button
    )
    black_overlay = create_black_overlay(page)
    # open_filter_view(menu)
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
