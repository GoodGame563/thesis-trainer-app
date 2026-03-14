from flet import Shimmer, ShimmerDirection, Theme


class CustomShimmer(Shimmer):
    def __init__(self, content, expand=None):
        super().__init__(
            content=content,
            base_color="#525252",
            # base_color= self.page.theme.color_scheme.outline ,
            highlight_color="#f5f5f5",
            # highlight_color=self.page.theme.color_scheme.secondary,
            direction=ShimmerDirection.LTR,
            period=1000,
            expand=expand,
        )
