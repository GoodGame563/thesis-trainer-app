from flet import (
    Button,
    ButtonStyle,
    Card,
    CardVariant,
    FilledButton,
    FloatingActionButton,
    Margin,
    RoundedRectangleBorder,
    Text,
    icons,
)

from .constants import ButtonType


def create_basic_text(value: str) -> Text:
    return Text(value, no_wrap=False, overflow="ELLIPSIS")


def create_biger_text(value: str) -> Text:
    return Text(value, no_wrap=False, overflow="ELLIPSIS", expand=True, size=18)


def create_bigest_text(value: str) -> Text:
    return Text(value, no_wrap=False, overflow="ELLIPSIS", expand=True, size=30)


def create_basic_text_block(value: str) -> Card:
    text = create_basic_text(value)
    text.margin = 5
    return Card(content=text, variant=CardVariant.OUTLINED, elevation=4)


def create_biger_text_block(value: str) -> Card:
    text = create_biger_text(value)
    text.margin = 5
    return Card(content=text, variant=CardVariant.OUTLINED, elevation=2)

def create_bigest_text_block(value: str) -> Card:
    text = create_biger_text(value)
    text.margin = 5
    return Card(content=text, variant=CardVariant.OUTLINED, elevation=2)


def create_basic_text_button(value: str, on_click=None) -> Button:
    return create_button(value, None, ButtonType.BASIC, on_click)


def create_action_text_button(value: str, on_click=None) -> Button:
    return create_button(value, None, ButtonType.ACTION, on_click)


def create_icon_button(icon: icons.Icons, on_click=None) -> FloatingActionButton:
    return create_button("", icon, ButtonType.BASIC, on_click)


def create_agree_text_button(value: str, on_click=None) -> Button:
    return create_button(value, None, ButtonType.AGREE, on_click)


def create_cancel_text_button(value: str, on_click=None) -> Button:
    return create_button(value, None, ButtonType.CANCEL, on_click)


def create_button(text: str, icon: icons.Icons, type: ButtonType, on_click) -> Button:
    style = ButtonStyle(shape=RoundedRectangleBorder(radius=8))
    size_margin = Margin.only(left=10, right=10, top=5, bottom=0)
    match type:
        case ButtonType.ACTION:
            return FilledButton(
                content=create_biger_text(text),
                style=style,
                elevation=10,
                margin=size_margin,
                height=50,
                on_click=on_click,
            )
        case ButtonType.BASIC:
            if icon is not None:
                return FloatingActionButton(
                    icon=icon,
                    shape=RoundedRectangleBorder(radius=20),
                    margin=20,
                    on_click=on_click,
                )
            return Button(
                icon=icon,
                content=create_biger_text(text),
                style=style,
                elevation=10,
                margin=size_margin,
                height=50,
                on_click=on_click,
            )
        case ButtonType.AGREE:
            pass
            # bgcolor = color_scheme.tertiary
        case ButtonType.CANCEL:
            pass
            # bgcolor = color_scheme.error
