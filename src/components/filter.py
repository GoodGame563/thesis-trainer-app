from click import style
from flet import (
    Animation,
    AnimationCurve,
    Button,
    Card,
    Column,
    Container,
    Dropdown,
    DropdownOption,
    ListView,
    Margin,
    Offset,
    Row,
    Switch,
    Text,
    TextField,
)

from models import (
    KpiRole,
    СomparisonType,
    filter_kpi,
    name_column_table,
    update_table,
    visible_column_table,
)
from utils import create_action_text_button, create_basic_text_button

from .overlay import close_overlay, open_overlay

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
        button = create_basic_text_button(value.comprasion, change_content_button)
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
            data=field,
            on_change=change_switch,
        )
        field.disabled = not switch.value
        positive_table.append(
            Card(
                content=Row(controls=[switch, button, field]),
                margin=Margin.only(
                    left=10,
                    right=10,
                    top=8,
                    bottom=0,
                ),
                key=key,
            )
        )
    return positive_table


def create_negative_table():
    negative_table = []
    for key, value in filter_kpi[selectKpiRole].negative_indicators.items():
        button = create_basic_text_button(value.comprasion, change_content_button)
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
            data=field,
            on_change=change_switch,
        )
        field.disabled = not switch.value
        negative_table.append(
            Card(
                content=Row(controls=[switch, button, field]),
                margin=Margin.only(
                    left=10,
                    right=10,
                    top=8,
                    bottom=0,
                ),
                key=key,
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


dropdown = Dropdown(
    value="ALL_ROLES", options=get_option(), on_select=select, margin=5, expand=True
)

positive_table = ListView(controls=[])
negative_table = ListView(controls=[])


column_table = []
for key, value in visible_column_table.items():
    column_table.append(
        Card(
            content=Switch(
                label=name_column_table[key],
                key=key,
                value=value,
            ),
            margin=Margin.only(
                left=10,
                right=10,
                top=8,
                bottom=0,
            ),
        )
    )

filter_name_block = Card(
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
)

middle_content_left_side = Container(
    content=Column(
        controls=[
            Card(
                content=Text(
                    "Что отображать",
                    no_wrap=False,
                    overflow="ELLIPSIS",
                    expand=True,
                    size=30,
                    text_align="center",
                    margin=10,
                ),
                margin=Margin.only(
                    left=10,
                    right=10,
                    top=10,
                    bottom=0,
                ),
            ),
            Card(
                content=ListView(controls=column_table, spacing=0),
                expand=True,
                margin=Margin.only(
                    left=10,
                    right=10,
                    top=0,
                    bottom=10,
                ),
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
            Card(
                content=Text(
                    "Подсчет KPI",
                    no_wrap=False,
                    overflow="ELLIPSIS",
                    expand=True,
                    size=30,
                    text_align="center",
                    margin=10,
                ),
                margin=Margin.only(
                    left=10,
                    right=10,
                    top=10,
                    bottom=0,
                ),
            ),
            Container(
                content=Row(
                    controls=[
                        Column(
                            controls=[
                                Card(
                                    content=Switch(
                                        label="Учитывать амплуа",
                                        key="check_role",
                                        # value=value,
                                    ),
                                    margin=Margin.only(
                                        left=10,
                                        right=10,
                                        top=10,
                                        bottom=0,
                                    ),
                                ),
                                Card(
                                    content=positive_table,
                                    margin=Margin.only(
                                        left=10,
                                        right=10,
                                        top=0,
                                        bottom=10,
                                    ),
                                    expand=True,
                                ),
                            ],
                            expand=1,
                            horizontal_alignment="STRETCH",
                        ),
                        Column(
                            controls=[
                                Card(
                                    content=dropdown,
                                    margin=Margin.only(
                                        left=10,
                                        right=10,
                                        top=10,
                                        bottom=0,
                                    ),
                                ),
                                Card(
                                    content=negative_table,
                                    margin=Margin.only(
                                        left=10,
                                        right=10,
                                        top=0,
                                        bottom=10,
                                    ),
                                    expand=True,
                                ),
                            ],
                            expand=1,
                            horizontal_alignment="STRETCH",
                        ),
                    ]
                ),
                expand=True,
                margin=Margin.only(
                    left=10,
                    right=10,
                    top=0,
                    bottom=10,
                ),
                border_radius=8,
            ),
        ],
        horizontal_alignment="STRETCH",
        spacing=10,
    ),
    expand=4,
)

middle_content_block = Card(
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
        Card(
            content=Container(
                content=Column(
                    controls=[
                        filter_name_block,
                        middle_content_block,
                        Row(
                            controls=[
                                create_action_text_button("Сохранить", safe_button)
                            ],
                            alignment="center",
                        ),
                    ],
                ),
                margin=10,
            ),
        )
    ),
    padding=30,
    offset=Offset(0, 1),
    animate_offset=Animation(300, AnimationCurve.EASE_IN_OUT),
)
