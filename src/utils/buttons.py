from flet import (
    Button,
    ButtonStyle,
    FilledButton,
    FloatingActionButton,
    Margin,
    RoundedRectangleBorder,
)

from models import ComparisonType

from .text import MenuText, NormalText


def change_content_button(e):
    match e.control.content.value:
        case ComparisonType.EQUALLY:
            e.control.content.value = ComparisonType.MORE
        case ComparisonType.MORE:
            e.control.content.value = ComparisonType.LESS
        case ComparisonType.LESS:
            e.control.content.value = ComparisonType.EQUALLY_MORE
        case ComparisonType.MORE:
            e.control.content.value = ComparisonType.EQUALLY_MORE
        case ComparisonType.EQUALLY_MORE:
            e.control.content.value = ComparisonType.EQUALLY_LESS
        case ComparisonType.EQUALLY_LESS:
            e.control.content.value = ComparisonType.EQUALLY


class ComparisonButton(Button):
    def __init__(self, text):
        super().__init__()
        self.style = ButtonStyle(shape=RoundedRectangleBorder(radius=8), padding=0)
        self.content = NormalText(text)
        self.on_click = change_content_button
        self.elevation = 3
        self.margin = 5
        self.height = 35
        self.width = 35
        self.key = "comprasion"

    def change_content_button(self):
        match self.value:
            case ComparisonType.EQUALLY:
                self.value = ComparisonType.MORE
            case ComparisonType.MORE:
                self.value = ComparisonType.LESS
            case ComparisonType.LESS:
                self.value = ComparisonType.EQUALLY_MORE
            case ComparisonType.MORE:
                self.value = ComparisonType.EQUALLY_MORE
            case ComparisonType.EQUALLY_MORE:
                self.value = ComparisonType.EQUALLY_LESS
            case ComparisonType.EQUALLY_LESS:
                self.value = ComparisonType.EQUALLY
        self.update()


class BasicButton(Button):
    def __init__(self, text, on_click=None, key=None):
        super().__init__()
        self.style = ButtonStyle(shape=RoundedRectangleBorder(radius=8))
        self.content = NormalText(text)
        self.on_click = on_click
        self.elevation = 8
        self.key = key


class MenuButton(Button):
    def __init__(self, text, on_click=None):
        super().__init__()
        self.style = ButtonStyle(shape=RoundedRectangleBorder(radius=8))
        self.content = MenuText(text)
        self.on_click = on_click
        self.elevation = 8
        self.margin = 4
        self.expand = 1


class IconButton(FloatingActionButton):
    def __init__(self, icon, on_click=None):
        super().__init__(
            icon=icon,
            shape=RoundedRectangleBorder(radius=20),
            margin=20,
            on_click=on_click,
        )


class BigBasicButton(Button):
    def __init__(self, text, on_click=None):
        super().__init__()
        self.style = ButtonStyle(shape=RoundedRectangleBorder(radius=8))
        self.content = NormalText(text)
        self.on_click = on_click
        self.elevation = 8


class ActionButton(FilledButton):
    def __init__(self, text, on_click=None, expand=False):
        super().__init__()
        self.style = ButtonStyle(shape=RoundedRectangleBorder(radius=8))
        self.content = NormalText(text)
        self.height = 50
        self.on_click = on_click
        self.elevation = 8
        self.margin = Margin.only(left=10, right=10, top=5, bottom=0)
        self.expand = expand
