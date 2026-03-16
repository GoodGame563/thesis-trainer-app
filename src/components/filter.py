import asyncio

from flet import (
    BottomSheet,
    Button,
    Column,
    Container,
    CrossAxisAlignment,
    Dropdown,
    DropdownOption,
    ExpansionPanel,
    ExpansionPanelList,
    ListView,
    MainAxisAlignment,
    PopupMenuButton,
    Row,
    ScrollMode,
    Switch,
)

from models import KpiRole, TableData, filter_kpi, name_column_table
from utils import (
    ActionButton,
    BigestTextBlock,
    CustomBSContentBlock,
    CustomShimmer,
    FilterList,
    NegativeSwitchTextFieldBlock,
    NormalText,
    PositiveSwitchTextFieldBlock,
    SlidingContentBlock,
    SwitchBlock,
    VisibleColumnsList,
)


class FilterButtomSheet(BottomSheet):
    selectKpiRole = KpiRole.ALL_ROLES

    def __init__(self, on_dismiss):
        self.positive_list_view = FilterList()
        self.negative_list_view = FilterList()
        self.switch_role_select = SwitchBlock(
            "Учитывать амплуа",
            False,
            None,
            "check_role",
            1,
        )
        self.column_list_view = VisibleColumnsList()
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
                            ("Что отображать", "Подсчет KPI"),  # type: ignore
                            [
                                self.column_list_view,
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
                                                    content=self.positive_list_view,
                                                    expand=1,
                                                    adaptive=True,
                                                ),
                                                ExpansionPanel(
                                                    header=NormalText(
                                                        "Негативные факторы"
                                                    ),
                                                    content=self.negative_list_view,
                                                    expand=1,
                                                ),
                                            ],
                                            spacing=10,
                                            expand=8,
                                            expanded_header_padding=4,
                                        ),
                                    ],
                                    horizontal_alignment=CrossAxisAlignment.STRETCH,
                                ),
                            ],
                            expand=6,
                        ),
                        Row(
                            controls=[ActionButton("Сохранить", self.safe_button)],
                            alignment=MainAxisAlignment.CENTER,
                            expand=1,
                        ),
                    ],
                ),
                margin=10,
            ),
            fullscreen=True,
            on_dismiss=on_dismiss,
        )

    def get_switch_role_value(self) -> bool:
        return self.switch_role_select.get_value()

    def get_filter_visible_column(self) -> dict[str, bool]:
        return self.column_list_view.get_value()

    async def set_data(self, visible_columns: dict[str, bool]):
        self.dropdown_container.content = Dropdown(
            value="ALL_ROLES",
            options=get_option(),
            on_select=self.select,
            margin=5,
            expand=True,
        )
        self.column_list_view.set_value(
            [
                SwitchBlock(name_column_table[key], value, None, key)
                for key, value in visible_columns.items()
            ]
        )
        await self.set_tables()

    def safe_button(self):
        self.page.pop_dialog()
        self.safe_tables()

    def safe_tables(self):
        for key, value in self.positive_list_view.get_value().items():
            filter_kpi[self.selectKpiRole].positive_indicators[key] = value
        for key, value in self.negative_list_view.get_value().items():
            filter_kpi[self.selectKpiRole].negative_indicators[key] = value

    async def set_tables(self):
        self.positive_list_view.set_value(
            [
                PositiveSwitchTextFieldBlock(
                    name_column_table[key],
                    value.enabled,
                    value.comprasion,
                    str(value.value),
                    key,
                )
                for key, value in filter_kpi[
                    self.selectKpiRole
                ].positive_indicators.items()
            ]
        )
        self.negative_list_view.set_value(
            [
                NegativeSwitchTextFieldBlock(
                    name_column_table[key],
                    value.enabled,
                    value.comprasion,
                    str(value.value),
                    key,
                )
                for key, value in filter_kpi[
                    self.selectKpiRole
                ].negative_indicators.items()
            ]
        )
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
