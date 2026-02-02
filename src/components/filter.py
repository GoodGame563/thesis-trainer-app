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
)

from models import (
    KpiRole,
    filter_kpi,
    name_column_table,
    update_table,
    visible_column_table,
)
from utils import (
    ActionButton,
    BigerTextBlock,
    BigestTextBlock,
    CustomBSContentBlock,
    NegativeSwitchTextFieldBlock,
    PositiveSwitchTextFieldBlock,
    SwitchBlock,
)

from .overlay import close_overlay, open_overlay

selectKpiRole = KpiRole.ALL_ROLES


def open_filter_view():
    filter_view.offset = Offset(0, 0)
    open_overlay()


def safe_button(e):
    for c in column_table:
        visible_column_table[c.content.key] = c.content.value
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
        positive_table.append(
            PositiveSwitchTextFieldBlock(
                name_column_table[key],
                value.enabled,
                value.comprasion,
                value.value,
                key,
            )
        )
    return positive_table


def create_negative_table():
    negative_table = []
    for key, value in filter_kpi[selectKpiRole].negative_indicators.items():
        negative_table.append(
            NegativeSwitchTextFieldBlock(
                name_column_table[key],
                value.enabled,
                value.comprasion,
                value.value,
                key,
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
                    element.on_change()
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
                    element.on_change()
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


positive_table = ListView(controls=[])
negative_table = ListView(controls=[])


column_table = []
for key, value in visible_column_table.items():
    column_table.append(SwitchBlock(name_column_table[key], value, None, key))

middle_content_left_side = Container(
    content=Column(
        controls=[
            BigerTextBlock("Что отображать"),
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
            BigerTextBlock("Подсчет KPI"),
            Container(
                content=Row(
                    controls=[
                        Column(
                            controls=[
                                SwitchBlock(
                                    "Учитывать амплуа", False, None, "check_role"
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
                                    content=Dropdown(
                                        value="ALL_ROLES",
                                        options=get_option(),
                                        on_select=select,
                                        margin=5,
                                        expand=True,
                                    ),
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

middle_content_block = CustomBSContentBlock(
    Row(
        controls=[
            middle_content_left_side,
            middle_content_right_side,
        ]
    ),
    8,
)
filter_view = Container(
    content=(
        Card(
            content=Container(
                content=Column(
                    controls=[
                        BigestTextBlock("Фильтр"),
                        middle_content_block,
                        Row(
                            controls=[ActionButton("Сохранить", safe_button)],
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
