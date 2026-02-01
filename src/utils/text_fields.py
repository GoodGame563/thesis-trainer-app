from flet import Margin, TextField


class SmallTextField(TextField):
    def __init__(self, value, key="value"):
        super().__init__()
        self.height = 35
        self.value = value
        self.content_padding = 0
        self.key = key
        self.expand = 1
        self.margin = Margin.only(right=5)
