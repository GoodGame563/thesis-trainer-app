from flet import Margin, TextField


class SmallTextField(TextField):
    def __init__(self, value: str, key="value"):
        super().__init__()
        self.height = 35
        self.value = value
        self.content_padding = 0
        self.key = key
        self.expand = 1
        self.margin = Margin.only(right=5)


class NormalTextField(TextField):
    def __init__(self, label: str, key="value", disabled=False):
        super().__init__()
        self.label = label
        self.content_padding = 2
        self.key = key
        self.expand = 1
        self.margin = Margin.only(left=10, right=10, top=5, bottom=0)
        self.disabled = disabled
