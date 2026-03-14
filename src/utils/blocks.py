from flet import Card, CardVariant, Column, Margin, Row, Tab, TabBar, TabBarView, Tabs, MainAxisAlignment, Text

from .buttons import ComparisonButton
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
        self.switch = PositiveColorSwitch(label, value_swith)
        self.content = Row(
            controls=[self.switch, ComparisonButton(value_button), self.field]
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
        self.switch = NegativeColorSwitch(label, value_swith)
        self.content = Row(
            controls=[self.switch, ComparisonButton(value_button), self.field]
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


class SwitchBlock(Card):
    def __init__(
        self,
        label: str,
        value_switch: bool,
        on_change=None,
        key="value",
        expand=None,
    ):
        super().__init__()
        self.content = NeutralColorSwitch(label, value_switch, on_change, key)
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


class CustomSSContentBlock(Card):
    def __init__(self, content, expand=None):
        super().__init__(
            content=content, expand=expand, elevation=4, variant=CardVariant.OUTLINED
        )


class BaseTextBlock(Card):
    def __inti__(self):
        super().__init__()
        self.inner_data = Text("")

    def change_text(self, text:str):
        self.inner_data.value = text
        self.inner_data.update()

class BigestTextBlock(BaseTextBlock):
    def __init__(self, text:str , expand=None):
        self.inner_data = BigestText(text)
        self.inner_data.margin = 5
        super().__init__(
            elevation=10,
            variant=CardVariant.OUTLINED,
            content=Row(
                controls=[
                    self.inner_data,
                ],
                alignment=MainAxisAlignment.CENTER,
                expand=True,
            ),
            expand=expand,
        )


class BigerTextBlock(BaseTextBlock):
    def __init__(self, text:str):
        self.inner_data = BigerText(text)
        super().__init__(
            elevation=8,
            variant=CardVariant.OUTLINED,
            content=self.inner_data,
            margin=Margin.only(
                left=10,
                right=10,
                top=10,
                bottom=0,
            ),
        )

class NormalTextBlock(BaseTextBlock):
    def __init__(self, text:str, expand=None):
        self.inner_data = NormalText(text)
        self.inner_data.margin = 5
        super().__init__(
            elevation=10,
            variant=CardVariant.OUTLINED,
            content=Row(
                controls=[
                    self.inner_data,
                ],
                alignment=MainAxisAlignment.CENTER,
                expand=True,
            ),
            expand=expand,
        )





class SlidingContentBlock(Card):
    def __init__(self, text_buttons: list[str], controls, expand=None):
        tabs = []
        for el in text_buttons:
            tabs.append(Tab(label=NormalText(el)))
        super().__init__(
            content=Tabs(
                length=len(controls),
                selected_index=0,
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
