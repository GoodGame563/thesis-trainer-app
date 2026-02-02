from flet import ControlState, Switch

from theme import light_cs


class PositiveColorSwitch(Switch):
    def __init__(self, label: str, value: bool, on_change, key="enabled"):
        super().__init__()
        self.label = label
        self.key = key
        self.value = value
        self.on_change = on_change
        self.thumb_color = {ControlState.SELECTED: light_cs.tertiary}

class NegativeColorSwitch(Switch):
    def __init__(self, label: str, value: bool, on_change, key="enabled"):
        super().__init__()
        self.label = label
        self.key = key
        self.value = value
        self.on_change = on_change
        self.thumb_color = {ControlState.SELECTED: light_cs.error}

class NeutralColorSwitch(Switch):
    def __init__(self, label: str, value: bool, on_change, key="enabled"):
        super().__init__()
        self.label = label
        self.key = key
        self.value = value
        self.on_change = on_change