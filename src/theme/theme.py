from flet import (
    ButtonStyle,
    ButtonTheme,
    CardTheme,
    ColorScheme,
    ControlState,
    DropdownTheme,
    FilledButtonTheme,
    FloatingActionButtonTheme,
    MenuStyle,
    SwitchTheme,
    TextStyle,
    TextTheme,
    Theme,
)

light_color = {
    "primary": "#0D1B2A",
    "accent": "#4CC9F0",
    "background": "#FFFFFF",
    "text_data": "#1B1B1B",
    "spliter": "#6B7280",
    "success": "#38B35B",
    "error": "#E63946",
    "shadow": "#000000",
}

light_cs = ColorScheme(
    primary=light_color["primary"],
    on_primary=light_color["background"],
    secondary=light_color["accent"],
    on_secondary=light_color["primary"],
    surface=light_color["background"],
    on_surface=light_color["text_data"],
    outline=light_color["spliter"],
    tertiary=light_color["success"],
    on_tertiary=light_color["background"],
    error=light_color["error"],
    on_error=light_color["background"],
    shadow=light_color["shadow"],
)
light_theme = Theme(
    color_scheme_seed="light",
    color_scheme=light_cs,
    scaffold_bgcolor=light_color["background"],
    divider_color=light_color["spliter"],
    card_bgcolor=light_color["background"],
    use_material3=True,
    filled_button_theme=FilledButtonTheme(
        style=ButtonStyle(bgcolor=light_color["accent"])
    ),
    button_theme=ButtonTheme(ButtonStyle(bgcolor=light_color["background"])),
    floating_action_button_theme=FloatingActionButtonTheme(
        bgcolor=light_color["background"],
        foreground_color=light_color["primary"],
        elevation=8,
    ),
    switch_theme=SwitchTheme(
        track_color=light_color["primary"],
        thumb_color={
            ControlState.SELECTED: light_color["accent"],
            ControlState.DISABLED: light_color["primary"],
            ControlState.ERROR: light_color["error"],
        },
    ),
    card_theme=CardTheme(
        shadow_color=light_color["shadow"],
        color=light_color["background"],
        elevation=8,
    ),
    dropdown_theme=DropdownTheme(
        menu_style=MenuStyle(
            elevation=8,
            bgcolor=light_color["background"],
            padding=5,
        )
    ),
    text_theme=TextTheme(
        body_large=TextStyle(color=light_color["primary"]),
        body_medium=TextStyle(color=light_color["primary"]),
        body_small=TextStyle(color=light_color["primary"]),
        display_large=TextStyle(color=light_color["primary"]),
        display_medium=TextStyle(color=light_color["primary"]),
        display_small=TextStyle(color=light_color["primary"]),
        headline_large=TextStyle(color=light_color["primary"]),
        headline_medium=TextStyle(color=light_color["primary"]),
        headline_small=TextStyle(color=light_color["primary"]),
        label_large=TextStyle(color=light_color["primary"]),
        label_medium=TextStyle(color=light_color["primary"]),
        label_small=TextStyle(color=light_color["primary"]),
        title_large=TextStyle(color=light_color["primary"]),
        title_medium=TextStyle(color=light_color["primary"]),
        title_small=TextStyle(color=light_color["primary"]),
    ),
)


dark_color = {
    "primary": "#E6F4FF",
    "accent": "#4CC9F0",
    "background": "#0D1217",
    "text_data": "#E2E8F0",
    "spliter": "#4B5563",
    "success": "#38B35B",
    "error": "#F15A60",
    "shadow": "#FFFFFF",
}

dark_cs = ColorScheme(
    primary=dark_color["primary"],
    on_primary=dark_color["background"],
    secondary=dark_color["accent"],
    on_secondary=dark_color["primary"],
    surface=dark_color["background"],
    on_surface=dark_color["text_data"],
    outline=dark_color["spliter"],
    tertiary=dark_color["success"],
    on_tertiary=dark_color["background"],
    error=dark_color["error"],
    on_error=dark_color["background"],
    shadow=dark_color["shadow"],
)
dark_theme = Theme(
    color_scheme_seed="dark",
    color_scheme=dark_cs,
    scaffold_bgcolor=dark_color["background"],
    divider_color=dark_color["spliter"],
    card_bgcolor=dark_color["background"],
    use_material3=True,
    button_theme=ButtonTheme(ButtonStyle(bgcolor=dark_color["background"])),
    floating_action_button_theme=FloatingActionButtonTheme(
        bgcolor=dark_color["background"], foreground_color=dark_color["primary"]
    ),
    switch_theme=SwitchTheme(
        track_color=dark_color["primary"],
        thumb_color={
            ControlState.SELECTED: dark_color["accent"],
            ControlState.DISABLED: dark_color["primary"],
        },
    ),
    card_theme=CardTheme(
        shadow_color=dark_color["shadow"],
        color=dark_color["background"],
        elevation=12,
        margin=5,
    ),
    dropdown_theme=DropdownTheme(
        menu_style=MenuStyle(
            elevation=8,
            bgcolor=dark_color["background"],
            padding=5,
        )
    ),
    filled_button_theme=FilledButtonTheme(
        style=ButtonStyle(bgcolor=dark_color["accent"])
    ),
    text_theme=TextTheme(
        body_large=TextStyle(color=dark_color["primary"]),
        body_medium=TextStyle(color=dark_color["primary"]),
        body_small=TextStyle(color=dark_color["primary"]),
        display_large=TextStyle(color=dark_color["primary"]),
        display_medium=TextStyle(color=dark_color["primary"]),
        display_small=TextStyle(color=dark_color["primary"]),
        headline_large=TextStyle(color=dark_color["primary"]),
        headline_medium=TextStyle(color=dark_color["primary"]),
        headline_small=TextStyle(color=dark_color["primary"]),
        label_large=TextStyle(color=dark_color["primary"]),
        label_medium=TextStyle(color=dark_color["primary"]),
        label_small=TextStyle(color=dark_color["primary"]),
        title_large=TextStyle(color=dark_color["primary"]),
        title_medium=TextStyle(color=dark_color["primary"]),
        title_small=TextStyle(color=dark_color["primary"]),
    ),
)
