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
    Dropdown
)

from utils import (
    create_basic_text_button,
    create_icon_button,
    create_action_text_button,
)


def create_menu(page: Page, close_menu) -> Row:
    return Row(
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




def create_filter_view(
    page: Page,
    base_shadow: BoxShadow,
    small_shadow,
    column_table: list,
    dropdown: Dropdown,
    safe_button,
) -> Container:
    positive_table = ListView(
        controls=[],
        spacing=0
    )
    negative_table = ListView(
        controls=[],
        spacing=0,
    )
    
    def select_element(e):
        for option in e.control.options:
            if option.key == e.control.value:
                e.control.data[0].controls = option.data[0]
                e.control.data[1].controls = option.data[1]
                break
        
        
    dropdown.on_select = select_element
    dropdown.data = [positive_table, negative_table]
    return Container(
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
                        shadow=[base_shadow],
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
                                                shadow=[base_shadow],
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
                                                shadow=[base_shadow],
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
                                                shadow=[base_shadow],
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
                                                                        # value=value,
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
                                                                        base_shadow
                                                                    ],
                                                                ),
                                                                Container(
                                                                    content=positive_table,
                                                                    bgcolor=page.theme.color_scheme.surface,
                                                                    margin=Margin.only(
                                                                        left=10,
                                                                        right=10,
                                                                        top=10,
                                                                        bottom=10,
                                                                    ),
                                                                    border_radius=8,
                                                                    shadow=[
                                                                        small_shadow
                                                                    ],
                                                                    expand=True,
                                                                ),
                                                            ],
                                                            expand=1,
                                                            horizontal_alignment="STRETCH",
                                                        ),
                                                        Column(
                                                            controls=[
                                                                Container(
                                                                    content=dropdown,
                                                                    bgcolor=page.theme.color_scheme.surface,
                                                                    margin=Margin.only(
                                                                        left=10,
                                                                        right=10,
                                                                        top=10,
                                                                        bottom=0,
                                                                    ),
                                                                    border_radius=8,
                                                                    shadow=[
                                                                        base_shadow
                                                                    ],
                                                                ),
                                                                Container(
                                                                    content=negative_table,
                                                                    bgcolor=page.theme.color_scheme.surface,
                                                                    margin=Margin.only(
                                                                        left=10,
                                                                        right=10,
                                                                        top=10,
                                                                        bottom=10,
                                                                    ),
                                                                    border_radius=8,
                                                                    shadow=[
                                                                        small_shadow
                                                                    ],
                                                                    expand=True,
                                                                ),

                                                            ],
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
                                                shadow=[base_shadow],
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
        shadow=[base_shadow],
        offset=Offset(0, 1),
        animate_offset=300,
    )


def create_black_overlay(page: Page) -> Container:
    return Container(
        bgcolor=Colors.with_opacity(0.1, page.theme.color_scheme.shadow),
        blur=5,
        visible=True,
        opacity=0.0,
        offset=Offset(-1, 0),
        animate_opacity=400,
    )
