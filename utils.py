from flet import (
    ElevatedButton,
    Text,
    ColorScheme,
    ButtonStyle,
    RoundedRectangleBorder,
    FloatingActionButton,
    IconButton,
    icons,
    margin,
)
from structs import ButtonType


def create_basic_text(value: str) -> Text:
    return Text(value, no_wrap=False, overflow="ELLIPSIS")


def create_biger_text(value: str) -> Text:
    return Text(value, no_wrap=False, overflow="ELLIPSIS", expand=True, size=18)


def create_bigest_text(value: str) -> Text:
    return Text(value, no_wrap=False, overflow="ELLIPSIS", expand=True, size=30)


def create_basic_text_button(
    value: str, color_scheme: ColorScheme, on_click=None
) -> ElevatedButton:
    return create_button(value, None, color_scheme, ButtonType.BASIC, on_click)


def create_action_text_button(
    value: str, color_scheme: ColorScheme, on_click=None
) -> ElevatedButton:
    return create_button(value, None, color_scheme, ButtonType.ACTION, on_click)


def create_icon_button(
    icon: icons.Icons, color_scheme: ColorScheme, on_click=None
) -> FloatingActionButton:
    return create_button("", icon, color_scheme, ButtonType.BASIC, on_click)


def create_agree_text_button(
    value: str, color_scheme: ColorScheme, on_click=None
) -> ElevatedButton:
    return create_button(value, None, color_scheme, ButtonType.AGREE, on_click)


def create_cancel_text_button(
    value: str, color_scheme: ColorScheme, on_click=None
) -> ElevatedButton:
    return create_button(value, None, color_scheme, ButtonType.CANCEL, on_click)


def create_button(
    text: str, icon: icons.Icons, color_scheme: ColorScheme, type: ButtonType, on_click
) -> ElevatedButton:
    style = ButtonStyle(shape=RoundedRectangleBorder(radius=8))
    size_margin = margin.only(left=10, right=10, top=5, bottom=0)
    bgcolor = None
    match type:
        case ButtonType.ACTION:
            bgcolor = color_scheme.secondary
        case ButtonType.BASIC:
            bgcolor = color_scheme.surface
        case ButtonType.AGREE:
            bgcolor = color_scheme.tertiary
        case ButtonType.CANCEL:
            bgcolor = color_scheme.error
    if icon is not None:
        return FloatingActionButton(
            icon=icon,
            bgcolor=bgcolor,
            shape=RoundedRectangleBorder(radius=20),
            foreground_color=color_scheme.primary,
            margin=20,
            on_click=on_click,
        )
    return ElevatedButton(
        icon=icon,
        content=create_biger_text(text),
        bgcolor=bgcolor,
        style=style,
        elevation=10,
        margin=size_margin,
        height=50,
        on_click=on_click,
    )
