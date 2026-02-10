from flet import Shimmer

class CustomShimmer(Shimmer):
    def __init__(self, content, expand= None):
        super().__init__(
            content=content,
            base_color="#e0e0e0",
            highlight_color="#f5f5f5",
            direction="LEFT_TO_RIGHT",
             period=1000,
             expand=expand
             )