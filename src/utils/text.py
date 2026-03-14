from flet import Text, TextOverflow, TextAlign


class NormalText(Text):
    def __init__(self, text: str, key: int | None = None):
        super().__init__(
            value=text,
            no_wrap=False,
            overflow=TextOverflow.ELLIPSIS,
            expand=True,
            size=18,
            key=key,
        )


class ComparisonText(Text):
    def __init__(self, text: str, key: int | None = None):
        super().__init__(
            value=text,
            no_wrap=False,
            overflow=TextOverflow.ELLIPSIS,
            expand=True,
            size=18,
            margin=2,
            key=key,
        )


class MenuText(Text):
    def __init__(self, text: str):
        super().__init__(
            value=text,
            no_wrap=False,
            overflow=TextOverflow.ELLIPSIS,
            expand=True,
            size=22,
            margin=10,
        )


class BigestText(Text):
    def __init__(self, text: str, text_align: TextAlign = TextAlign.CENTER):
        super().__init__(
            value=text,
            no_wrap=False,
            overflow=TextOverflow.ELLIPSIS,
            expand=True,
            size=40,
            text_align=text_align,
        )


class BigerText(Text):
    def __init__(self, text: str, text_align: TextAlign = TextAlign.CENTER):
        super().__init__(
            value=text,
            no_wrap=False,
            overflow=TextOverflow.ELLIPSIS,
            expand=True,
            size=30,
            text_align=text_align,
            margin=8,
        )
