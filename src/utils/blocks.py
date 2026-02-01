from flet import Card, Row, Margin, CardVariant
from .switchs import PositiveColorSwitch
from .text_fields import SmallTextField
from .buttons import СomparisonButton

class PositiveSwitchTextFieldBlock(Card):
    def __init__(self,label:str,value_swith:bool, value_button:str,value_field:str, key = "value"):
        super().__init__()
        self.field = SmallTextField(value_field)
        self.switch = PositiveColorSwitch(label, value_swith, self.change_switch)
        self.field.disabled = not self.switch.value
        self.content = Row(controls=[self.switch, СomparisonButton(value_button), self.field])
        self.margin = Margin.only(
                    left=10,
                    right=10,
                    top=8,
                    bottom=0,
                )
        self.key = key
        self.variant=CardVariant.OUTLINED
        self.elevation = 4
    def change_switch(self):
        self.field.disabled = not self.switch.value