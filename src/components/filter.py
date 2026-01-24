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
    DropdownOption,
    TextField,
    Button,
)

from utils import (
    create_basic_text_button,
    create_icon_button,
    create_action_text_button,
)

from .overlay import open_overlay, close_overlay

from theme import AppTheme, base_shadow, small_shadow
from models import (
    create_basic_text,
    СomparisonType,
    name_column_table,
    visible_column_table,
    update_table,
    filter_kpi,
    KpiRole,
)

selectKpiRole = KpiRole.ALL_ROLES


def open_filter_view():
    filter_view.offset = Offset(0, 0)
    open_overlay()


def change_switch(e):
    e.control.data.disabled = not e.control.value


def change_current_switch(e):
    e.data.disabled = not e.value


def change_content_button(e):
    match e.control.content.value:
        case СomparisonType.EQUALLY:
            e.control.content.value = СomparisonType.MORE
        case СomparisonType.MORE:
            e.control.content.value = СomparisonType.LESS
        case СomparisonType.LESS:
            e.control.content.value = СomparisonType.EQUALLY_MORE
        case СomparisonType.MORE:
            e.control.content.value = СomparisonType.EQUALLY_MORE
        case СomparisonType.EQUALLY_MORE:
            e.control.content.value = СomparisonType.EQUALLY_LESS
        case СomparisonType.EQUALLY_LESS:
            e.control.content.value = СomparisonType.EQUALLY


def safe_button(e):
    for c in column_table:
        visible_column_table[c.content.key] = c.content.value
    safe_tables()
    update_table()
    close_overlay()
    filter_view.offset = Offset(0, 1)


def get_option():
    options = []
    for role in KpiRole:
        options.append(DropdownOption(key=role.name, text=role.value))
    return options


def create_filter_view() -> Container:
    positive_table.controls = create_positive_table()
    negative_table.controls = create_negative_table()
    return filter_view


def create_positive_table():
    positive_table = []
    for key, value in filter_kpi[selectKpiRole].positive_indicators.items():
        button = create_basic_text_button(
            value.comprasion, AppTheme.color_scheme, change_content_button
        )
        button.style.padding = 0
        button.margin = 5
        button.width = 35
        button.height = 35
        button.key = "comprasion"
        field = TextField(
            height=35,
            value=value.value,
            content_padding=0,
            key="value",
            expand=1,
            margin=Margin.only(right=5),
        )
        switch = Switch(
            label=name_column_table[key],
            key="enabled",
            value=value.enabled,
            thumb_color={
                ControlState.SELECTED: AppTheme.color_scheme.tertiary,
                ControlState.DISABLED: AppTheme.color_scheme.primary,
            },
            data=field,
            track_color=AppTheme.color_scheme.primary,
            on_change=change_switch,
        )
        field.disabled = not switch.value
        positive_table.append(
            Container(
                content=Row(controls=[switch, button, field]),
                bgcolor=AppTheme.color_scheme.surface,
                margin=Margin.only(
                    left=10,
                    right=10,
                    top=8,
                    bottom=0,
                ),
                key=key,
                border_radius=8,
                shadow=[small_shadow],
            )
        )
    return positive_table


def create_negative_table():
    negative_table = []
    for key, value in filter_kpi[selectKpiRole].negative_indicators.items():
        button = create_basic_text_button(
            value.comprasion, AppTheme.color_scheme, change_content_button
        )
        button.style.padding = 0
        button.margin = 5
        button.width = 35
        button.height = 35
        button.key = "comprasion"
        field = TextField(
            height=35,
            value=value.value,
            content_padding=0,
            key="value",
            expand=1,
            margin=Margin.only(right=5),
        )
        switch = Switch(
            label=name_column_table[key],
            key="enabled",
            value=value.enabled,
            thumb_color={
                ControlState.SELECTED: AppTheme.color_scheme.error,
                ControlState.DISABLED: AppTheme.color_scheme.primary,
            },
            data=field,
            track_color=AppTheme.color_scheme.primary,
            on_change=change_switch,
        )
        field.disabled = not switch.value
        negative_table.append(
            Container(
                content=Row(controls=[switch, button, field]),
                bgcolor=AppTheme.color_scheme.surface,
                margin=Margin.only(
                    left=10,
                    right=10,
                    top=8,
                    bottom=0,
                ),
                key=key,
                border_radius=8,
                shadow=[small_shadow],
            )
        )
    return negative_table


def update_tables(new_role: KpiRole):
    safe_tables()
    global selectKpiRole
    selectKpiRole = new_role
    set_tables()


def set_tables():
    for c in positive_table.controls:
        for element in c.content.controls:
            match element:
                case Button():
                    element.content.value = getattr(
                        filter_kpi[selectKpiRole].positive_indicators[c.key],
                        element.key,
                    )
                case Switch():
                    element.value = getattr(
                        filter_kpi[selectKpiRole].positive_indicators[c.key],
                        element.key,
                    )
                    change_current_switch(element)
                case _:
                    element.value = getattr(
                        filter_kpi[selectKpiRole].positive_indicators[c.key],
                        element.key,
                    )
    for c in negative_table.controls:
        for element in c.content.controls:
            match element:
                case Button():
                    element.content.value = getattr(
                        filter_kpi[selectKpiRole].negative_indicators[c.key],
                        element.key,
                    )
                case Switch():
                    element.value = getattr(
                        filter_kpi[selectKpiRole].negative_indicators[c.key],
                        element.key,
                    )
                    change_current_switch(element)
                case _:
                    element.value = getattr(
                        filter_kpi[selectKpiRole].negative_indicators[c.key],
                        element.key,
                    )


def safe_tables():
    for c in positive_table.controls:
        for element in c.content.controls:
            value = None
            match element:
                case Button():
                    value = element.content.value
                case _:
                    value = element.value
            setattr(
                filter_kpi[selectKpiRole].positive_indicators[c.key], element.key, value
            )
    for c in negative_table.controls:
        for element in c.content.controls:
            value = None
            match element:
                case Button():
                    value = element.content.value
                case _:
                    value = element.value
            setattr(
                filter_kpi[selectKpiRole].negative_indicators[c.key], element.key, value
            )


def select(e):
    update_tables(KpiRole[e.data])
    # global selectKpiRole
    # selectKpiRole = KpiRole[e.data]


dropdown = Dropdown(
    value="ALL_ROLES",
    options=get_option(),
    bgcolor=AppTheme.color_scheme.surface,
    on_select=select,
)

positive_table = ListView(controls=[])
negative_table = ListView(controls=[])


column_table = []
for key, value in visible_column_table.items():
    column_table.append(
        Container(
            content=Switch(
                label=name_column_table[key],
                key=key,
                value=value,
                thumb_color={
                    ControlState.SELECTED: AppTheme.color_scheme.secondary,
                    ControlState.DISABLED: AppTheme.color_scheme.primary,
                },
                track_color=AppTheme.color_scheme.primary,
            ),
            bgcolor=AppTheme.color_scheme.surface,
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

filter_name_block = Container(
    bgcolor=AppTheme.color_scheme.surface,
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
)

middle_content_left_side = Container(
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
                bgcolor=AppTheme.color_scheme.surface,
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
                content=ListView(controls=column_table, spacing=0),
                expand=True,
                padding=10,
                bgcolor=AppTheme.color_scheme.surface,
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
)

middle_content_right_side = Container(
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
                bgcolor=AppTheme.color_scheme.surface,
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
                                            ControlState.SELECTED: AppTheme.color_scheme.secondary,
                                            ControlState.DISABLED: AppTheme.color_scheme.primary,
                                        },
                                        track_color=AppTheme.color_scheme.primary,
                                    ),
                                    bgcolor=AppTheme.color_scheme.surface,
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
                                    content=positive_table,
                                    bgcolor=AppTheme.color_scheme.surface,
                                    margin=Margin.only(
                                        left=10,
                                        right=10,
                                        top=10,
                                        bottom=10,
                                    ),
                                    border_radius=8,
                                    shadow=[small_shadow],
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
                                    bgcolor=AppTheme.color_scheme.surface,
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
                                    content=negative_table,
                                    bgcolor=AppTheme.color_scheme.surface,
                                    margin=Margin.only(
                                        left=10,
                                        right=10,
                                        top=10,
                                        bottom=10,
                                    ),
                                    border_radius=8,
                                    shadow=[small_shadow],
                                    expand=True,
                                ),
                            ],
                            expand=1,
                            horizontal_alignment="STRETCH",
                        ),
                    ]
                ),
                expand=True,
                bgcolor=AppTheme.color_scheme.surface,
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
)

middle_content_block = Container(
    bgcolor=AppTheme.color_scheme.surface,
    expand=8,
    content=Row(
        controls=[
            middle_content_left_side,
            middle_content_right_side,
        ]
    ),
)

filter_view = Container(
    content=(
        Column(
            controls=[
                filter_name_block,
                middle_content_block,
                Row(
                    controls=[
                        create_action_text_button(
                            "Сохранить", AppTheme.color_scheme, safe_button
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
    bgcolor=AppTheme.color_scheme.surface,
    clip_behavior="ANTI_ALIAS_WITH_SAVE_LAYER",
    shadow=[base_shadow],
    offset=Offset(0, 1),
    animate_offset=300,
)
