import asyncio

import aioshutil
from flet import (
    AlertDialog,
    Card,
    CardVariant,
    Column,
    Container,
    FilePicker,
    FilePickerFileType,
    MainAxisAlignment,
    Margin,
    Row,
    Text,
    TextField,
)

from db_controls import create_teams
from utils import ActionButton, BasicButton


class TeamDialog(AlertDialog):
    def __init__(self):
        self.path_file = ""
        self.command_field = TextField(
            content_padding=2,
            # key="value",
            label="Название",
            margin=Margin.only(left=10, right=10, top=5, bottom=0),
            expand=True,
        )
        super().__init__(
            content=Container(
                content=Column(
                    controls=[
                        Card(
                            content=Text(
                                "Создать команду",
                                no_wrap=False,
                                overflow="ELLIPSIS",
                                expand=True,
                                size=30,
                                text_align="center",
                                margin=10,
                            ),
                            margin=Margin.only(
                                left=10,
                                right=10,
                                top=10,
                                bottom=0,
                            ),
                            clip_behavior=True,
                            variant=CardVariant.OUTLINED,
                        ),
                        Row(
                            controls=[
                                self.command_field,
                                BasicButton("Загрузить лого", self.select_logo),
                            ]
                        ),
                        ActionButton("Сохранить", self.save),
                    ],
                    alignment=MainAxisAlignment.SPACE_EVENLY,
                    expand=True,
                    horizontal_alignment="STRETCH",
                ),
                margin=10,
                width=700,
                height=300,
                expand=True,
            ),
        )

    async def upload_file(self, e):
        print(e)

    async def save(self):
        self.open = False
        await asyncio.sleep(0.2)
        await create_teams(self.command_field.value, self.path_file)

    async def select_logo(self):
        f_p = FilePicker(on_upload=self.upload_file)
        file = await f_p.pick_files(
            file_type=FilePickerFileType.IMAGE,
            allow_multiple=False,
        )
        if len(file) == 0:
            return
        await aioshutil.copy2(file[0].path, ".\\assets\\logo_" + file[0].name)
        self.path_file = "logo_" + file[0].name
        await asyncio.sleep(0.1)

    # animate_offset=Animation(300, AnimationCurve.EASE_IN_OUT),
