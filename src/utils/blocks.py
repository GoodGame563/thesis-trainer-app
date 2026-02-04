from typing import Tuple
from flet import (
    Card,
    CardVariant,
    Column,
    Margin,
    Row,
    CupertinoSlidingSegmentedButton,
    Tab,
    TabBar,
    TabBarView,
    Tabs,
)

from .buttons import СomparisonButton
from .switchs import NegativeColorSwitch, NeutralColorSwitch, PositiveColorSwitch
from .text import BigerText, BigestText, NormalText
from .text_fields import SmallTextField


class PositiveSwitchTextFieldBlock(Card):
    def __init__(
        self,
        label: str,
        value_swith: bool,
        value_button: str,
        value_field: str,
        key="value",
    ):
        super().__init__()
        self.field = SmallTextField(value_field)
        self.switch = PositiveColorSwitch(label, value_swith, self.change_switch)
        self.field.disabled = not self.switch.value
        self.content = Row(
            controls=[self.switch, СomparisonButton(value_button), self.field]
        )
        self.margin = Margin.only(
            left=10,
            right=10,
            top=8,
            bottom=0,
        )
        self.key = key
        self.variant = CardVariant.OUTLINED
        self.elevation = 4

    def change_switch(self):
        self.field.disabled = not self.switch.value


class NegativeSwitchTextFieldBlock(Card):
    def __init__(
        self,
        label: str,
        value_swith: bool,
        value_button: str,
        value_field: str,
        key="value",
    ):
        super().__init__()
        self.field = SmallTextField(value_field)
        self.switch = NegativeColorSwitch(label, value_swith, self.change_switch)
        self.field.disabled = not self.switch.value
        self.content = Row(
            controls=[self.switch, СomparisonButton(value_button), self.field]
        )
        self.margin = Margin.only(
            left=10,
            right=10,
            top=8,
            bottom=0,
        )
        self.key = key
        self.variant = CardVariant.OUTLINED
        self.elevation = 4

    def change_switch(self):
        self.field.disabled = not self.switch.value


class SwitchBlock(Card):
    def __init__(
        self,
        label: str,
        value_swith: bool,
        on_change=None,
        key="value",
        expand=None,
    ):
        super().__init__()
        self.content = NeutralColorSwitch(label, value_swith, on_change, key)
        self.margin = Margin.only(
            left=10,
            right=10,
            top=8,
            bottom=0,
        )
        self.variant = CardVariant.OUTLINED
        self.elevation = 4
        self.expand = expand


class CustomBSContentBlock(Card):
    def __init__(self, content, expand=None):
        super().__init__(
            content=content, expand=expand, elevation=8, variant=CardVariant.OUTLINED
        )


class BigestTextBlock(Card):
    def __init__(self, text, expand=None):
        data = BigestText(text)
        data.margin = 5
        super().__init__(
            elevation=10,
            variant=CardVariant.OUTLINED,
            content=Row(
                controls=[
                    data,
                ],
                alignment="center",
                expand=True,
            ),
            expand=expand,
        )


class BigerTextBlock(Card):
    def __init__(self, text):
        data = BigerText(text)
        super().__init__(
            elevation=8,
            variant=CardVariant.OUTLINED,
            content=Row(
                controls=[
                    data,
                ],
                alignment="center",
                expand=True,
            ),
            margin=Margin.only(
                left=10,
                right=10,
                top=10,
                bottom=0,
            ),
        )


class SlidingContentBlock(Card):
    def __init__(self, text_buttons: Tuple[str], controls, expand=None):
        tabs = []
        for el in text_buttons:
            tabs.append(Tab(label=NormalText(el)))
        super().__init__(
            content=Tabs(
                length=len(controls),
                selected_index=1,
                expand=True,
                content=Column(
                    expand=True,
                    controls=[
                        TabBar(tabs=tabs),
                        TabBarView(controls=controls, expand=2),
                    ],
                ),
            ),
            expand=expand,
        )
