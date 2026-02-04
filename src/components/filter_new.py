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
    BottomSheet,
    CupertinoSlidingSegmentedButton,
    VerticalDivider,
    BoxConstraints,
    Colors,
    ResponsiveRow,
    ExpansionPanelList,
    ExpansionPanel,
)

from models import KpiRole, filter_kpi, name_column_table
from utils import (
    ActionButton,
    BigerTextBlock,
    BigestTextBlock,
    CustomBSContentBlock,
    InformationTable,
    NegativeSwitchTextFieldBlock,
    PositiveSwitchTextFieldBlock,
    SwitchBlock,
    NormalText,
    SlidingContentBlock,
)
from .overlay import close_overlay, open_overlay


class FilterButtomSheet(BottomSheet):
    selectKpiRole = KpiRole.ALL_ROLES

    def __init__(self, visible_columns: dict[str, bool], set_column):
        self.set = set_column
        self.positive_table = ListView(
            controls=[
                PositiveSwitchTextFieldBlock(
                    name_column_table[key],
                    value.enabled,
                    value.comprasion,
                    value.value,
                    key,
                )
                for key, value in filter_kpi[
                    self.selectKpiRole
                ].positive_indicators.items()
            ]
        )
        self.negative_table = ListView(
            controls=[
                NegativeSwitchTextFieldBlock(
                    name_column_table[key],
                    value.enabled,
                    value.comprasion,
                    value.value,
                    key,
                )
                for key, value in filter_kpi[
                    self.selectKpiRole
                ].negative_indicators.items()
            ]
        )
        self.column_table = [
            SwitchBlock(name_column_table[key], value, self.change_switch, key)
            for key, value in visible_columns.items()
        ]
        super().__init__(
            content=Container(
                content=Column(
                    controls=[
                        BigestTextBlock("Фильтр", 1),
                        SlidingContentBlock(
                            ("Что отображать", "Подсчет KPI"),
                            [
                                ListView(controls=self.column_table, spacing=0),
                                Column(
                                    controls=[
                                        Row(
                                            controls=[
                                                SwitchBlock(
                                                    "Учитывать амплуа",
                                                    False,
                                                    None,
                                                    "check_role",
                                                    1,
                                                ),
                                                CustomBSContentBlock(
                                                    Dropdown(
                                                        value="ALL_ROLES",
                                                        options=get_option(),
                                                        on_select=self.select,
                                                        margin=5,
                                                        expand=True,
                                                    ),
                                                    1,
                                                ),
                                            ],
                                            expand=1,
                                        ),
                                        ExpansionPanelList(
                                            controls=[
                                                ExpansionPanel(
                                                    header=NormalText(
                                                        "Позитивные факторы"
                                                    ),
                                                    content=ListView(
                                                        controls=[
                                                            self.positive_table,
                                                        ],
                                                        scroll="ALWAYS",
                                                        height=300,
                                                        expand=1,
                                                    ),
                                                    expand=1,
                                                ),
                                                ExpansionPanel(
                                                    header=NormalText(
                                                        "Негативные факторы"
                                                    ),
                                                    content=ListView(
                                                        controls=[
                                                            self.negative_table,
                                                        ],
                                                        scroll="",
                                                        expand=1,
                                                    ),
                                                    expand=1,
                                                ),
                                            ],
                                            spacing=10,
                                            expand=7,
                                            expanded_header_padding=4,
                                        ),
                                    ],
                                    horizontal_alignment="STRETCH",
                                ),
                            ],
                            expand=6,
                        ),
                        Row(
                            controls=[ActionButton("Сохранить", self.safe_button)],
                            alignment="center",
                            expand=1,
                        ),
                    ],
                ),
            ),
            #     margin=10,
            # ),
            # fullscreen=True,
            # size_constraints=BoxConstraints(min_width=1000, max_width=1000),
            # adaptive=True,
            scrollable=True,
            # padding=30,
            # offset=Offset(0, 1),
            # animate_offset=Animation(300, AnimationCurve.EASE_IN_OUT),
        )

    def change_switch(self, e):
        self.set(e.control.key, e.control.value)

    def open_filter_view(self):
        self.offset = Offset(0, 0)
        # open_overlay()

    def safe_button(self, e):
        # print(e.control)
        # for c in self.column_table:
        #     self.connected_table.visible_column_table[c.content.key] = c.content.value
        # self.connected_table.update()
        # close_overlay()
        self.offset = Offset(0, 1)

    def safe_tables(self):
        for c in self.positive_table.controls:
            for element in c.content.controls:
                value = None
                match element:
                    case Button():
                        value = element.content.value
                    case _:
                        value = element.value
                setattr(
                    filter_kpi[self.selectKpiRole].positive_indicators[c.key],
                    element.key,
                    value,
                )
        for c in self.negative_table.controls:
            for element in c.content.controls:
                value = None
                match element:
                    case Button():
                        value = element.content.value
                    case _:
                        value = element.value
                setattr(
                    filter_kpi[self.selectKpiRole].negative_indicators[c.key],
                    element.key,
                    value,
                )

    def set_tables(self):
        for c in self.positive_table.controls:
            for element in c.content.controls:
                match element:
                    case Button():
                        element.content.value = getattr(
                            filter_kpi[self.selectKpiRole].positive_indicators[c.key],
                            element.key,
                        )
                    case Switch():
                        element.value = getattr(
                            filter_kpi[self.selectKpiRole].positive_indicators[c.key],
                            element.key,
                        )
                        element.on_change()
                    case _:
                        element.value = getattr(
                            filter_kpi[self.selectKpiRole].positive_indicators[c.key],
                            element.key,
                        )
        for c in self.negative_table.controls:
            for element in c.content.controls:
                match element:
                    case Button():
                        element.content.value = getattr(
                            filter_kpi[self.selectKpiRole].negative_indicators[c.key],
                            element.key,
                        )
                    case Switch():
                        element.value = getattr(
                            filter_kpi[self.selectKpiRole].negative_indicators[c.key],
                            element.key,
                        )
                        element.on_change()
                    case _:
                        element.value = getattr(
                            filter_kpi[self.selectKpiRole].negative_indicators[c.key],
                            element.key,
                        )

    def update_tables(self, new_role: KpiRole):
        self.safe_tables()
        self.selectKpiRole = new_role
        self.set_tables()

    def select(self, e):
        self.update_tables(KpiRole[e.data])


def get_option():
    options = []
    for role in KpiRole:
        options.append(DropdownOption(key=role.name, text=role.value))
    return options
