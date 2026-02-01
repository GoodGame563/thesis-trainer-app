from flet import Button, ButtonStyle, RoundedRectangleBorder, Margin
from models import СomparisonType
from .text import NormalText

def change_content_button(e):
    match e.control.content.value:
        case СomparisonType.EQUALLY:
            e.control.content.value = СomparisonType.MORE
        case СomparisonType.MORE:
            e.control.content.value = СomparisonType.LESS
        case СomparisonType.LESS:
            e.control.content.value = СomparisonType.EQUALLY_MORE
        case СomparisonType.MORE:
            e.control.content.value = СomparisonType.EQUALLY_MORE
        case СomparisonType.EQUALLY_MORE:
            e.control.content.value = СomparisonType.EQUALLY_LESS
        case СomparisonType.EQUALLY_LESS:
            e.control.content.value = СomparisonType.EQUALLY


class СomparisonButton(Button):
    def __init__(self, text):
        super().__init__()
        self.style = ButtonStyle(shape=RoundedRectangleBorder(radius=8), padding=0)
        self.content = NormalText(text)
        self.on_click = change_content_button
        self.elevation=3
        self.margin=5
        self.height=35
        self.width=35
        self.key = "comprasion"

class BasicButton(Button):
    def __init__(self, text, on_click = None):
        super().__init__()
        self.style = ButtonStyle(shape=RoundedRectangleBorder(radius=8))
        self.content = NormalText(text)
        self.on_click = on_click

