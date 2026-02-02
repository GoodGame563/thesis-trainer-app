from flet import Card, CardVariant, Margin, Row

from .buttons import СomparisonButton
from .switchs import NegativeColorSwitch, NeutralColorSwitch, PositiveColorSwitch
from .text import BigerText, BigestText
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


class CustomBSContentBlock(Card):
    def __init__(self, content, expand=None):
        super().__init__(
            content=content, expand=expand, elevation=8, variant=CardVariant.OUTLINED
        )


class BigestTextBlock(Card):
    def __init__(self, text):
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
