from flet import Container, Offset, Colors

from theme import AppTheme

overlay = Container(
    bgcolor=Colors.with_opacity(0.2, AppTheme.color_scheme.shadow),
    blur=5,
    visible=True,
    opacity=0.0,
    offset=Offset(-1, 0),
    animate_opacity=500,
    animate_offset=10,
)


def create_black_overlay() -> Container:
    return overlay


def close_overlay():
    overlay.opacity = 0.0
    overlay.offset = Offset(-1, 0)


def open_overlay():
    overlay.offset = Offset(0, 0)
    overlay.opacity = 1.0
