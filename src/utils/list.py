from flet import ListView, ScrollMode

from models import ValueIndicators

from .blocks import (
    NegativeSwitchTextFieldBlock,
    PositiveSwitchTextFieldBlock,
    SwitchBlock,
)
from .shimmer import CustomShimmer


class PlayerList(ListView):
    def __init__(self):
        super().__init__()

    def get_value(self, value: list[str]):
        pass

    def set_value(self, value: list[str]):
        pass


class FilterList(ListView):
    def __init__(self):
        self.info: list[PositiveSwitchTextFieldBlock | NegativeSwitchTextFieldBlock] = (
            []
        )

        super().__init__(
            scroll=ScrollMode.ALWAYS,
            height=300,
            expand=1,
            controls=[CustomShimmer(SwitchBlock("wait", False)) for _ in range(10)],
            spacing=1,
        )

    def get_value(self) -> dict[str, ValueIndicators]:
        indicators: dict[str, ValueIndicators] = {}
        for el in self.info:
            indicators[el.get_key()] = ValueIndicators(
                el.get_comparison(), el.get_value(), el.get_enabled()
            )
        return indicators

    def set_value(
        self, value: list[PositiveSwitchTextFieldBlock | NegativeSwitchTextFieldBlock]
    ):
        self.info.clear()
        self.info.extend(value)
        self.controls.clear()
        self.controls.extend(self.info)
        self.update()


class VisibleColumnsList(ListView):
    def __init__(self):
        self.info: list[SwitchBlock] = []
        super().__init__(
            controls=[CustomShimmer(SwitchBlock("wait", False)) for _ in range(10)],
            spacing=0,
        )

    def get_value(self) -> dict[str, bool]:
        result = {}
        for el in self.info:
            result[el.get_key()] = el.get_value()
        return result

    def set_value(self, value: list[SwitchBlock]):
        self.info.clear()
        self.info.extend(value)
        self.controls.clear()
        self.controls.extend(self.info)
        self.update()
