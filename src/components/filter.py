from flet import (
    Animation,
    AnimationCurve,
    BottomSheet,
    BoxConstraints,
    Button,
    Card,
    Colors,
    Column,
    Container,
    CupertinoSlidingSegmentedButton,
    Dropdown,
    DropdownOption,
    ExpansionPanel,
    ExpansionPanelList,
    ListView,
    Margin,
    Offset,
    ResponsiveRow,
    Row,
    Switch,
    VerticalDivider,
)

from models import KpiRole, filter_kpi, name_column_table
from utils import (
    ActionButton,
    BigerTextBlock,
    BigestTextBlock,
    CustomBSContentBlock,
    InformationTable,
    NegativeSwitchTextFieldBlock,
    NormalText,
    PositiveSwitchTextFieldBlock,
    SlidingContentBlock,
    SwitchBlock,
)

from .overlay import close_overlay, open_overlay


class FilterButtomSheet(BottomSheet):
    selectKpiRole = KpiRole.ALL_ROLES

    def __init__(self, on_dismiss):
        self.positive_table = ListView(
            controls=[],
            scroll="ALWAYS",
            height=300,
            expand=1,
        )
        self.negative_table = ListView(
            controls=[],
            scroll="ALWAYS",
            height=300,
            expand=1,
        )

        self.column_table = []
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
                                        ),
                                        ExpansionPanelList(
                                            controls=[
                                                ExpansionPanel(
                                                    header=NormalText(
                                                        "Позитивные факторы"
                                                    ),
                                                    content=self.positive_table,
                                                    expand=1,
                                                ),
                                                ExpansionPanel(
                                                    header=NormalText(
                                                        "Негативные факторы"
                                                    ),
                                                    content=self.negative_table,
                                                    expand=1,
                                                ),
                                            ],
                                            spacing=10,
                                            expand=8,
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
                margin=10,
            ),
            fullscreen=True,
            on_dismiss=on_dismiss,
        )

    async def set_data(self, visible_columns):
        self.column_table.extend(
            [
                SwitchBlock(name_column_table[key], value, None, key)
                for key, value in visible_columns.items()
            ]
        )
        self.positive_table.controls.extend(
            [
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

        self.negative_table.controls.extend(
            [
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

    def change_switch(self, e):
        self.set(e.control.key, e.control.value)

    def safe_button(self, e):

        self.parent.page.pop_dialog()

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
