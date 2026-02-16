import asyncio

from flet import (
    BottomSheet,
    Button,
    Column,
    Container,
    Dropdown,
    DropdownOption,
    ExpansionPanel,
    ExpansionPanelList,
    ListView,
    PopupMenuButton,
    Row,
    Switch,
)

from models import KpiRole, filter_kpi, name_column_table
from utils import (
    ActionButton,
    BigestTextBlock,
    CustomBSContentBlock,
    CustomShimmer,
    NegativeSwitchTextFieldBlock,
    NormalText,
    PositiveSwitchTextFieldBlock,
    SlidingContentBlock,
    SwitchBlock,
)


class FilterButtomSheet(BottomSheet):
    selectKpiRole = KpiRole.ALL_ROLES

    def __init__(self, on_dismiss):
        self.positive_table_container = Container(
            content=CustomShimmer(
                ListView(
                    controls=[SwitchBlock("Wait", True) for _ in range(10)],
                    scroll="ALWAYS",
                    height=300,
                    expand=1,
                )
            )
        )
        self.negative_table_container = Container(
            content=CustomShimmer(
                ListView(
                    controls=[SwitchBlock("Wait", True) for _ in range(10)],
                    scroll="ALWAYS",
                    height=300,
                    expand=1,
                )
            )
        )
        self.switch_role_select = SwitchBlock(
            "Учитывать амплуа",
            False,
            None,
            "check_role",
            1,
        )

        self.column_table_container = Container(
            content=CustomShimmer(
                ListView(
                    controls=[SwitchBlock("Wait", True) for _ in range(10)], spacing=0
                )
            )
        )
        self.dropdown_container = Container(
            content=CustomShimmer(
                Dropdown(
                    value="Wait",
                    options=[DropdownOption(text="Wait") for _ in range(10)],
                    margin=5,
                    expand=True,
                )
            )
        )
        super().__init__(
            content=Container(
                content=Column(
                    controls=[
                        BigestTextBlock("Фильтр", 1),
                        SlidingContentBlock(
                            ("Что отображать", "Подсчет KPI"),
                            [
                                self.column_table_container,
                                Column(
                                    controls=[
                                        Row(
                                            controls=[
                                                self.switch_role_select,
                                                CustomBSContentBlock(
                                                    self.dropdown_container,
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
                                                    content=self.positive_table_container,
                                                    expand=1,
                                                ),
                                                ExpansionPanel(
                                                    header=NormalText(
                                                        "Негативные факторы"
                                                    ),
                                                    content=self.negative_table_container,
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
        self.dropdown_container.content = Dropdown(
            value="ALL_ROLES",
            options=get_option(),
            on_select=self.select,
            margin=5,
            expand=True,
        )

        self.column_table_container.content = ListView(
            controls=[
                SwitchBlock(name_column_table[key], value, None, key)
                for key, value in visible_columns.items()
            ],
            spacing=0,
        )
        self.positive_table_container.content = ListView(
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
            ],
            scroll="ALWAYS",
            height=300,
            expand=1,
        )
        self.negative_table_container.content = ListView(
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
            ],
            scroll="ALWAYS",
            height=300,
            expand=1,
        )

    def change_switch(self, e):
        self.set(e.control.key, e.control.value)

    def safe_button(self, e):
        self.parent.page.pop_dialog()
        self.safe_tables()

    def safe_tables(self):
        for c in self.positive_table_container.content.controls:
            for element in c.content.controls:
                value = None
                match element:
                    case PopupMenuButton():
                        value = element.content.value
                    case _:
                        value = element.value
                setattr(
                    filter_kpi[self.selectKpiRole].positive_indicators[c.key],
                    element.key,
                    value,
                )
        for c in self.negative_table_container.content.controls:
            for element in c.content.controls:
                value = None
                match element:
                    case PopupMenuButton():
                        value = element.content.value
                    case _:
                        value = element.value
                setattr(
                    filter_kpi[self.selectKpiRole].negative_indicators[c.key],
                    element.key,
                    value,
                )

    async def set_tables(self):
        for c in self.positive_table_container.content.controls:
            for element in c.content.controls:
                match element:
                    case PopupMenuButton():
                        element.content.value = getattr(
                            filter_kpi[self.selectKpiRole].positive_indicators[c.key],
                            element.key,
                        )
                    case Switch():
                        element.value = getattr(
                            filter_kpi[self.selectKpiRole].positive_indicators[c.key],
                            element.key,
                        )
                    case _:
                        element.value = getattr(
                            filter_kpi[self.selectKpiRole].positive_indicators[c.key],
                            element.key,
                        )
        for c in self.negative_table_container.content.controls:
            for element in c.content.controls:
                match element:
                    case PopupMenuButton():
                        element.content.value = getattr(
                            filter_kpi[self.selectKpiRole].negative_indicators[c.key],
                            element.key,
                        )
                    case Switch():
                        element.value = getattr(
                            filter_kpi[self.selectKpiRole].negative_indicators[c.key],
                            element.key,
                        )
                    case _:
                        element.value = getattr(
                            filter_kpi[self.selectKpiRole].negative_indicators[c.key],
                            element.key,
                        )
        self.positive_table_container.update()
        self.negative_table_container.update()
        await asyncio.sleep(0.2)

    async def update_tables(self, new_role: KpiRole):
        self.safe_tables()
        self.selectKpiRole = new_role
        await self.set_tables()

    async def select(self, e):
        await self.update_tables(KpiRole[e.data])


def get_option():
    options = []
    for role in KpiRole:
        options.append(DropdownOption(key=role.name, text=role.value))
    return options
