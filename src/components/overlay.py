from flet import Colors, Container, Offset

from theme import dark_theme, light_theme

overlay = Container()


def create_black_overlay() -> Container:
    global overlay
    overlay = Container(
        blur=5,
        visible=True,
        opacity=0.0,
        offset=Offset(-1, 0),
        animate_opacity=500,
        animate_offset=10,
        bgcolor=Colors.with_opacity(0.2, light_theme.color_scheme.shadow),
    )
    return overlay


def close_overlay():
    overlay.opacity = 0.0
    overlay.offset = Offset(-1, 0)


def open_overlay():
    overlay.offset = Offset(0, 0)
    overlay.opacity = 1.0
