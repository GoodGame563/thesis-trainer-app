import asyncio

from flet import (
    Button,
    Column,
    Container,
    CupertinoBottomSheet,
    CupertinoPicker,
    FilledButton,
    CrossAxisAlignment
)

from .buttons import ActionButton
from .shimmer import CustomShimmer
from .text import NormalText


class Picker(CupertinoBottomSheet):
    def __init__(self, activation_button: Button | FilledButton, dissmiss_func=None):
        self.picker = CupertinoPicker(
            controls=[CustomShimmer(NormalText("Wait")) for _ in range(10)],
            expand=5,
            selected_index=0,
            magnification=1.22,
            squeeze=1.2,
            use_magnifier=True,
        )

        async def save_data():
            self.open = False
            self.update()
            activation_button.content = self.picker.controls[self.picker.selected_index]
            activation_button.update()

        super().__init__(
            content=Container(
                content=Column(
                    controls=[
                        self.picker,
                        ActionButton("Сохранить", save_data, 1),
                    ],
                    horizontal_alignment=CrossAxisAlignment.CENTER,
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
        self.picker.controls.clear()
        self.picker.controls.extend(data)
        self.picker.update()
