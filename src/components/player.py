import asyncio

import aioshutil
from flet import (
    AlertDialog,
    Card,
    CardVariant,
    Column,
    Container,
    DatePicker,
    FilePicker,
    FilePickerFileType,
    MainAxisAlignment,
    Margin,
    Row,
    Text,
    TextField,
)

from db_controls import create_player
from models import Player
from utils import ActionButton, BasicButton, NormalTextField


class PlayerAddDialog(AlertDialog):
    def __init__(self):
        self.path_file = ""
        self.full_name_field = NormalTextField(
            "Полное ФИО",
        )
        self.height_field = NormalTextField(
            "Рост (см)",
        )
        self.weight_field = NormalTextField(
            "Вес (кг)",
        )
        self.date_birth_field = NormalTextField(
            disabled=True,
            label="Дата рождения",
        )
        self.photo_path_field = NormalTextField(
            "Путь к фото",
            disabled=True,
        )
        self.photo_path_field.value = ""
        self.photo_path_field.expand = True
        super().__init__(
            content=Container(
                content=Column(
                    controls=[
                        Card(
                            content=Text(
                                "Добавить игрока",
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
                                self.full_name_field,
                            ],
                            expand=1,
                        ),
                        Row(
                            controls=[
                                self.height_field,
                                self.weight_field,
                            ],
                            expand=1,
                        ),
                        Row(
                            controls=[
                                self.date_birth_field,
                                BasicButton(
                                    "Выбрать дату рождения", self.select_date_birth
                                ),
                            ],
                            expand=1,
                        ),
                        Row(
                            controls=[
                                BasicButton("Загрузить фото", self.select_photo),
                                self.photo_path_field,
                            ],
                            expand=1,
                        ),
                        ActionButton("Сохранить", self.save),
                    ],
                    expand=True,
                    horizontal_alignment="STRETCH",
                ),
                margin=10,
                width=700,
                height=400,
                expand=True,
            ),
        )

    async def select_date_birth(self, e):
        async def close_date_picker(d):
            self.date_birth_field.value = d.data.strftime("%d.%m.%Y")
            self.date_birth_field.update()
            await asyncio.sleep(0.2)

        dp = DatePicker(
            cancel_text="Отмена",
            confirm_text="Выбрать",
            error_format_text="Неверный формат даты",
            error_invalid_text="Неверная дата",
            help_text="Выберите дату",
            on_change=close_date_picker,
        )
        self.page.show_dialog(dp)
        await asyncio.sleep(0.2)

    async def select_photo(self, e):
        f_p = FilePicker()
        file = await f_p.pick_files(
            file_type=FilePickerFileType.IMAGE,
            allow_multiple=False,
        )
        if len(file) == 0:
            return
        await aioshutil.copy2(file[0].path, ".\\assets\\photo_" + file[0].name)
        self.path_file = "photo_" + file[0].name
        self.photo_path_field.value = self.path_file
        self.photo_path_field.update()
        await asyncio.sleep(0.1)

    async def save(self):
        if (
            not self.full_name_field.value
            or not self.height_field.value
            or not self.weight_field.value
            or not self.date_birth_field.value
            or not self.photo_path_field.value
        ):
            return

        try:
            height = int(self.height_field.value)
            weight = int(self.weight_field.value)
        except ValueError:
            return

        self.open = False
        await asyncio.sleep(0.2)
        await create_player(
            Player(
                id=0,
                full_name=self.full_name_field.value,
                height=height,
                weight=weight,
                birth_date=self.date_birth_field.value,
                path_to_photo=self.photo_path_field.value,
            )
        )
