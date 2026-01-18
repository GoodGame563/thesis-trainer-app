from flet import (
    Page,
    run,
    DataTable,
    DataColumn,
    DataRow,
    DataCell,
    Text,
    Theme,
    ColorScheme,
    AppBar,
    IconButton,
    FloatingActionButton,
    FloatingActionButtonLocation,
    icons,
    Column,
    Container,
    SnackBar,
    RoundedRectangleBorder,
    BoxShadow,
    Offset,
    Animation,
    Row,
    NavigationDrawer,
    NavigationDrawerDestination,
    Icon,
    Divider,
    ElevatedButton,
    app,
    Pagelet,
    Button,
    Stack,
    ButtonStyle,
    Colors,
    AnimationCurve,
    Margin,
    ListView,
    CrossAxisAlignment,
    Switch,
    ControlState,
)
import logging
from theme import light_theme, dark_theme, light_cs, dark_cs
from structs import Role, Player, Team
from table import (
    create_table,
    TableData,
    visible_column_table,
    name_column_table,
    update_table,
)
from datetime import date
from utils import (
    create_basic_text_button,
    create_action_text_button,
    create_icon_button,
    create_agree_text_button,
    create_cancel_text_button,
    create_biger_text,
    create_bigest_text,
)

logging.basicConfig(level=logging.INFO)


def main(page: Page):

    def open_menu(e):
        logging.info("Menu opened")
        menu.offset = Offset(0, 0)
        black_overlay.offset = Offset(0, 0)
        black_overlay.opacity = 1.0
        page.update()

    def close_menu(e):
        logging.info("Menu closed")
        black_overlay.offset = Offset(-1, 0)
        black_overlay.opacity = 0.0
        menu.offset = Offset(-1, 0)
        page.update()

    def open_filter_page(e):
        filter_page.offset = Offset(0, 0)
        black_overlay.offset = Offset(0, 0)
        black_overlay.opacity = 1.0
        page.update()

    def safe_button(e):
        for c in column_table:
            visible_column_table[c.content.key] = c.content.value
        update_table(table)
        filter_page.offset = Offset(0, 1)
        black_overlay.offset = Offset(-1, 0)
        black_overlay.opacity = 0.0
        table.update()
        page.update()

    logging.getLogger("flet_core").setLevel(logging.INFO)
    page.title = "Таблица с фильтром"
    page.padding = 0
    is_dark = {"value": False}
    page.theme = dark_theme if is_dark["value"] else light_theme

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
                shadow=[
                    BoxShadow(
                        color=Colors.with_opacity(
                            0.5,
                            page.theme.color_scheme.shadow,
                        ),
                        offset=Offset(0, 0),
                        blur_radius=8,
                        blur_style="OUTER",
                    )
                ],
            )
        )

    table = create_table(
        [
            TableData(
                player=Player(
                    nst="Иванов Иван Иванович",
                    weight=85.0,
                    height=190.0,
                    team=Team(name="Рубин"),
                    birth_date=date(1990, 5, 15),
                ),
                role=Role.NOTHING,
                minutes_played=0,
                passes_accurate=0,
                passes_inaccurate=0,
                captures_done=0,
                captures_missed=0,
                rakov_cleared=0,
                tackles_done=0,
                meters_covered=0,
                defenders_beaten=0,
                breakthroughs=0,
                attempts_grounded=0,
                realizations_scored=0,
                realizations_attempted=0,
                penalties_scored=0,
                penalties_attempted=0,
                dropgoals_scored=0,
                dropgoals_attempted=0,
                points_scored=0,
                penalties_received=0,
                loss_ball=0,
                yellow_cards=0,
                red_cards=0,
                passes_percent=0.0,
                captures_percent=0.0,
                realizations_percent=0.0,
                penalties_percent=0.0,
                dropgoals_percent=0.0,
            ),
            TableData(
                player=Player(
                    nst="Иванов Иван Иванович",
                    weight=85.0,
                    height=190.0,
                    team=Team(name="Рубин"),
                    birth_date=date(1990, 5, 15),
                ),
                role=Role.NOTHING,
                minutes_played=0,
                passes_accurate=0,
                passes_inaccurate=0,
                captures_done=0,
                captures_missed=0,
                rakov_cleared=0,
                tackles_done=0,
                meters_covered=0,
                defenders_beaten=0,
                breakthroughs=0,
                attempts_grounded=0,
                realizations_scored=0,
                realizations_attempted=0,
                penalties_scored=0,
                penalties_attempted=0,
                dropgoals_scored=0,
                dropgoals_attempted=0,
                points_scored=0,
                penalties_received=0,
                loss_ball=0,
                yellow_cards=0,
                red_cards=0,
                passes_percent=0.0,
                captures_percent=0.0,
                realizations_percent=0.0,
                penalties_percent=0.0,
                dropgoals_percent=0.0,
            ),
        ],
        page.theme.color_scheme,
        visible_column_table,
    )
    black_overlay = Container(
        bgcolor=Colors.with_opacity(0.1, page.theme.color_scheme.shadow),
        blur=5,
        visible=True,
        opacity=0.0,
        offset=Offset(-1, 0),
        animate_opacity=400,
    )
    menu = Row(
        controls=[
            Container(
                content=Column(
                    controls=[
                        create_basic_text_button(
                            "Добавить игрока", page.theme.color_scheme
                        ),
                        create_basic_text_button(
                            "Добавить матч", page.theme.color_scheme
                        ),
                        create_basic_text_button(
                            "Создать команду", page.theme.color_scheme
                        ),
                        create_basic_text_button("Трансфер", page.theme.color_scheme),
                        create_basic_text_button(
                            "Открыть статистику",
                            page.theme.color_scheme,
                        ),
                    ],
                    spacing=10,
                    horizontal_alignment="STRETCH",
                    width=300,
                ),
                bgcolor=page.theme.color_scheme.outline,
                padding=20,
            ),
            create_icon_button(icons.Icons.CLOSE, page.theme.color_scheme, close_menu),
        ],
        vertical_alignment="start",
        spacing=2,
        offset=Offset(-1, 0),
        animate_offset=Animation(300, AnimationCurve.EASE_OUT),
    )

    filter_page = Container(
        content=(
            Column(
                controls=[
                    Container(
                        bgcolor=page.theme.color_scheme.surface,
                        content=Row(
                            controls=[
                                Text(
                                    "Фильтр",
                                    no_wrap=False,
                                    overflow="ELLIPSIS",
                                    expand=True,
                                    size=40,
                                    text_align="center",
                                )
                            ],
                            alignment="center",
                            expand=True,
                        ),
                        border_radius=8,
                        shadow=[
                            BoxShadow(
                                color=Colors.with_opacity(
                                    0.5, page.theme.color_scheme.shadow
                                ),
                                offset=Offset(0, 0),
                                blur_radius=10,
                                blur_style="OUTER",
                            )
                        ],
                        margin=10,
                    ),
                    Container(
                        bgcolor=page.theme.color_scheme.surface,
                        expand=8,
                        content=Row(
                            controls=[
                                Container(
                                    content=Column(
                                        controls=[
                                            Container(
                                                content=Text(
                                                    "Что отображать",
                                                    no_wrap=False,
                                                    overflow="ELLIPSIS",
                                                    expand=True,
                                                    size=30,
                                                    text_align="center",
                                                    margin=10,
                                                ),
                                                bgcolor=page.theme.color_scheme.surface,
                                                margin=Margin.only(
                                                    left=10,
                                                    right=10,
                                                    top=10,
                                                    bottom=0,
                                                ),
                                                border_radius=8,
                                                shadow=[
                                                    BoxShadow(
                                                        color=Colors.with_opacity(
                                                            0.5,
                                                            page.theme.color_scheme.shadow,
                                                        ),
                                                        offset=Offset(0, 0),
                                                        blur_radius=8,
                                                        blur_style="OUTER",
                                                    )
                                                ],
                                            ),
                                            Container(
                                                content=ListView(
                                                    controls=column_table, spacing=0
                                                ),
                                                expand=True,
                                                padding=10,
                                                bgcolor=page.theme.color_scheme.surface,
                                                margin=Margin.only(
                                                    left=10,
                                                    right=10,
                                                    top=0,
                                                    bottom=10,
                                                ),
                                                shadow=[
                                                    BoxShadow(
                                                        color=Colors.with_opacity(
                                                            0.5,
                                                            page.theme.color_scheme.shadow,
                                                        ),
                                                        offset=Offset(0, 0),
                                                        blur_radius=10,
                                                        blur_style="OUTER",
                                                    )
                                                ],
                                                border_radius=8,
                                            ),
                                        ],
                                        horizontal_alignment="STRETCH",
                                        spacing=10,
                                    ),
                                    expand=2,
                                ),
                                Container(
                                    content=Column(
                                        controls=[
                                            Container(
                                                content=Text(
                                                    "Подсчет KPI",
                                                    no_wrap=False,
                                                    overflow="ELLIPSIS",
                                                    expand=True,
                                                    size=30,
                                                    text_align="center",
                                                    margin=10,
                                                ),
                                                bgcolor=page.theme.color_scheme.surface,
                                                margin=Margin.only(
                                                    left=10,
                                                    right=10,
                                                    top=10,
                                                    bottom=0,
                                                ),
                                                border_radius=8,
                                                shadow=[
                                                    BoxShadow(
                                                        color=Colors.with_opacity(
                                                            0.5,
                                                            page.theme.color_scheme.shadow,
                                                        ),
                                                        offset=Offset(0, 0),
                                                        blur_radius=8,
                                                        blur_style="OUTER",
                                                    )
                                                ],
                                            ),
                                            Container(
                                                content=Row(
                                                    controls=[
                                                        Column(
                                                            controls=[
                                                                Container(
                                                                    content=Switch(
                                                                        label="Учитывать амплуа",
                                                                        key="check_role",
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
                                                                        top=10,
                                                                        bottom=0,
                                                                    ),
                                                                    border_radius=8,
                                                                    shadow=[
                                                                        BoxShadow(
                                                                            color=Colors.with_opacity(
                                                                                0.5,
                                                                                page.theme.color_scheme.shadow,
                                                                            ),
                                                                            offset=Offset(
                                                                                0, 0
                                                                            ),
                                                                            blur_radius=8,
                                                                            blur_style="OUTER",
                                                                        )
                                                                    ],
                                                                ),
                                                                Container(
                                                                    content=Switch(
                                                                        label="Учитывать амплуа",
                                                                        key="check_role",
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
                                                                        top=10,
                                                                        bottom=0,
                                                                    ),
                                                                    border_radius=8,
                                                                    shadow=[
                                                                        BoxShadow(
                                                                            color=Colors.with_opacity(
                                                                                0.5,
                                                                                page.theme.color_scheme.shadow,
                                                                            ),
                                                                            offset=Offset(
                                                                                0, 0
                                                                            ),
                                                                            blur_radius=8,
                                                                            blur_style="OUTER",
                                                                        )
                                                                    ],
                                                                ),
                                                            ],
                                                            expand=1,
                                                            horizontal_alignment="STRETCH",
                                                        ),
                                                        Column(
                                                            controls=[],
                                                            expand=1,
                                                            horizontal_alignment="STRETCH",
                                                        ),
                                                    ]
                                                ),
                                                expand=True,
                                                bgcolor=page.theme.color_scheme.surface,
                                                margin=Margin.only(
                                                    left=10,
                                                    right=10,
                                                    top=0,
                                                    bottom=10,
                                                ),
                                                shadow=[
                                                    BoxShadow(
                                                        color=Colors.with_opacity(
                                                            0.5,
                                                            page.theme.color_scheme.shadow,
                                                        ),
                                                        offset=Offset(0, 0),
                                                        blur_radius=10,
                                                        blur_style="OUTER",
                                                    )
                                                ],
                                                border_radius=8,
                                            ),
                                        ],
                                        horizontal_alignment="STRETCH",
                                        spacing=10,
                                    ),
                                    expand=4,
                                ),
                            ]
                        ),
                    ),
                    Row(
                        controls=[
                            create_action_text_button(
                                "Сохранить", page.theme.color_scheme, safe_button
                            )
                        ],
                        alignment="center",
                    ),
                ],
                # expand=True
            )
        ),
        margin=30,
        padding=10,
        border_radius=16,
        bgcolor=page.theme.color_scheme.surface,
        clip_behavior="ANTI_ALIAS_WITH_SAVE_LAYER",
        shadow=[
            BoxShadow(
                color=page.theme.color_scheme.shadow,
                offset=Offset(0, 0),
                blur_radius=6,
                blur_style="OUTER",
            )
        ],
        offset=Offset(0, 0),
        animate_offset=300,
    )

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
                        shadow=[
                            BoxShadow(
                                color=page.theme.color_scheme.shadow,
                                offset=Offset(0, 0),
                                blur_radius=12.8,
                                blur_style="OUTER",
                            )
                        ],
                        expand=True,
                    ),
                    Container(
                        content=create_icon_button(
                            icons.Icons.FILTER_LIST,
                            page.theme.color_scheme,
                            open_filter_page,
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
                    filter_page,
                    menu,
                ]
            ),
            expand=True,
            clip_behavior="ANTI_ALIAS_WITH_SAVE_LAYER",
        )
    )


if __name__ == "__main__":
    run(main)
