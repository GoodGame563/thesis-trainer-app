import asyncio
import select

from flet import (
    Button,
    ButtonStyle,
    FilledButton,
    FloatingActionButton,
    Margin,
    PopupMenuButton,
    PopupMenuItem,
    RoundedRectangleBorder,
)

from models import ComparisonType

from .text import ComparisonText, MenuText, NormalText


class ComparisonButton(PopupMenuButton):
    def __init__(self, text: str):
        super().__init__(
            style=ButtonStyle(shape=RoundedRectangleBorder(radius=8), padding=0),
            content=ComparisonText(text),
            elevation=3,
            margin=5,
            height=35,
            width=35,
            key="comprasion",
            items=[
                PopupMenuItem(content=ComparisonType.EQUALLY, on_click=self.select),
                PopupMenuItem(content=ComparisonType.MORE, on_click=self.select),
                PopupMenuItem(content=ComparisonType.LESS, on_click=self.select),
                PopupMenuItem(
                    content=ComparisonType.EQUALLY_MORE, on_click=self.select
                ),
                PopupMenuItem(
                    content=ComparisonType.EQUALLY_LESS, on_click=self.select
                ),
            ],
        )

    async def select(self, e):
        self.content.value = e.control.content
        self.update()
        await asyncio.sleep(0.2)


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
