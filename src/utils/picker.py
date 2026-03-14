import asyncio

from flet import (
    Button,
    Column,
    Container,
    CupertinoBottomSheet,
    CupertinoPicker,
    FilledButton,
)

from .buttons import ActionButton
from .shimmer import CustomShimmer
from .text import NormalText


class Picker(CupertinoBottomSheet):
    def __init__(self, activation_button: Button | FilledButton, dissmiss_func=None):
        picker = CupertinoPicker(
            controls=[CustomShimmer(NormalText("Wait")) for _ in range(10)],
            expand=5,
            selected_index=2,
            magnification=1.22,
            squeeze=1.2,
            use_magnifier=True,
        )

        async def save_data():
            self.open = False
            self.update()
            activation_button.content = picker.controls[picker.selected_index]
            activation_button.update()

        super().__init__(
            content=Container(
                content=Column(
                    controls=[
                        picker,
                        ActionButton("Сохранить", save_data, 1),
                    ],
                    horizontal_alignment="CENTER",
                    height=300,
                ),
                margin=10,
                expand=1,
            ),
            height=216,
            padding=10,
            modal=True,
            on_dismiss=dissmiss_func,
        )

    async def set_data(self, data: list[NormalText]):
        picker = self.content.content.controls[0]
        picker.controls = data
        picker.update()
