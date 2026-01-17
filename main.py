from flet import (
    Page,
    run,
    DataTable,
    DataColumn,
    DataRow,
    DataCell,
    Text,
    Theme,
    ColorScheme,
    AppBar,
    IconButton,
    FloatingActionButton,
    FloatingActionButtonLocation,
    icons,
    Column,
    Container,
    SnackBar,
    RoundedRectangleBorder,
    BoxShadow,
    Offset,
    Animation,
    Row,
    NavigationDrawer, 
    NavigationDrawerDestination,
    Icon,
    Divider,
    ElevatedButton, app,
    Pagelet,
    Button,
    Stack,
)
import logging
from theme import light_theme, dark_theme, light_cs, dark_cs
from structs import Role, Player, Team
from table import create_table, TableData
from datetime import date
logging.basicConfig(level=logging.DEBUG)
def main(page: Page):
    logging.getLogger("flet_core").setLevel(logging.INFO)
    page.title = "Таблица с фильтром"
    page.padding = 20
    is_dark = {"value": False}
    page.theme = dark_theme if is_dark["value"] else light_theme

    table = create_table([
        TableData(
            player=Player(
                nst="Иванов Иван Иванович", weight=85.0, height=190.0,
                team=Team(name="Рубин"), birth_date=date(1990, 5, 15)
            ),
            date_birth=None,
            role=Role.NOTHING,
            minutes_played=0,
            passes_accurate=0,
            passes_inaccurate=0,
            captures_done=0,
            captures_missed=0,
            rakov_cleared=0,
            tackles_done=0,
            meters_covered=0,
            defenders_beaten=0,
            breakthroughs=0,
            attempts_grounded=0,
            realizations_scored=0,
            realizations_attempted=0,
            penalties_scored=0,
            penalties_attempted=0,
            dropgoals_scored=0,
            dropgoals_attempted=0,
            points_scored=0,
            penalties_received=0,
            turnovers=0,
            yellow_cards=0,
            red_cards=0, 
            passes_percent=0.0,
            captures_percent=0.0,
            realizations_percent=0.0,
            penalties_percent=0.0,
            dropgoals_percent=0.0,
        )
    ], page.theme.color_scheme)

    # layout = Container(
    #     content= wrapper, 
    #     bgcolor=page.theme.scaffold_bgcolor,
    #     expand=True,
    # )
    fab = FloatingActionButton(
        icon=icons.Icons.FILTER_LIST,
        tooltip="Фильтр",
        bgcolor=page.theme.color_scheme.secondary,
        foreground_color="white",
        # offset=Offset(4,4),
        shape=RoundedRectangleBorder(radius=20),
        # on_click=on_filter_click,
        elevation=6,
    )
    menu = FloatingActionButton(
        icon=icons.Icons.FILTER_LIST,
        tooltip="Фильтр",
        bgcolor=page.theme.color_scheme.secondary,
        foreground_color="white",
        # offset=Offset(4,4),
        shape=RoundedRectangleBorder(radius=20),
        # on_click=on_filter_click,
        elevation=6,
    )
    page.add(
        Container(
            Stack(
                controls=[
                    Container(
                        padding=0,
                        expand=True,
                        content=Column( 
                            controls=Row(
                                controls=table, 
                                scroll="AUTO",
                                ),
                                scroll="AUTO",
                                expand=True,),
                        bgcolor=page.theme.color_scheme.surface,
                        clip_behavior="none",
                        animate=Animation(250),
                        border_radius=16,
                        margin=10,
                        shadow=[
                            BoxShadow(
                                color=page.theme.color_scheme.shadow,
                                offset=Offset(0, 0),
                                blur_radius=12.8,
                                blur_style="OUTER",
                            )
                        ],
                    ),
                    Container(
                        content=menu,
                        left=0,
                        top=0,
                    )
                ]
            ),
            expand=True,
        )
    )
    page.floating_action_button = fab
    # page.floating_action_button_location = FloatingActionButtonLocation.END_FLOATING
    

if __name__ == "__main__":
    run(main)                