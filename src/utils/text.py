from flet import Text


class NormalText(Text):
    def __init__(self, text):
        super().__init__()
        self.value = text
        self.no_wrap = False
        self.overflow = "ELLIPSIS"
        self.expand = True
        self.size = 18


class BigestText(Text):
    def __init__(self, text, text_align = "center"):
        super().__init__()
        self.value = text
        self.no_wrap = False
        self.overflow = "ELLIPSIS"
        self.expand = True
        self.size = 40
        self.text_align = text_align

class BigerText(Text):
    def __init__(self, text, text_align = "center"):
        super().__init__()
        self.value = text
        self.no_wrap = False
        self.overflow = "ELLIPSIS"
        self.expand = True
        self.size = 30
        self.text_align = text_align
        self.margin = 8 