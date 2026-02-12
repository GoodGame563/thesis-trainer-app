import asyncio
from typing import List
from flet import (
    Column,
    Container,
    CupertinoPicker,
    CupertinoBottomSheet,
    Button,
    FilledButton,
    CupertinoActionSheet,
    CupertinoActionSheetAction,
)
from .shimmer import CustomShimmer
from .text import NormalText
from .buttons import ActionButton


class Picker(CupertinoBottomSheet):
    def __init__(self, activation_button: Button | FilledButton):
        picker = CupertinoPicker(
                            controls=[CustomShimmer(NormalText("Wait")) for _ in range(10)],
                            expand=5,
                            selected_index=3,
                            magnification=1.22,
                            squeeze=1.2,
                            use_magnifier=True,
                        )

        async def save_data():
            self.open = False
            self.update()
            await asyncio.sleep(0.2)
            activation_button.content = picker.controls[picker.selected_index]
            activation_button.update()
            
        super().__init__(
            content=Container(
                content= Column(
                    controls=[
                        picker,
                        ActionButton("Сохранить", save_data, 1),
                    ],
                    horizontal_alignment="CENTER",
                    height=300,
                ),
                margin=10,
                expand=1
            ),
            height=216,
            padding=10,
            modal=True
        )

    async def set_data(self, data: List[NormalText]):
        picker = self.content.content.controls[0]
        picker.controls = data
        picker.update()

