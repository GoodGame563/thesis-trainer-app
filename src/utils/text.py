from flet import Text 

class NormalText(Text):
    def __init__(self, text):
        super().__init__()
        self.value = text
        self.no_wrap=False
        self.overflow="ELLIPSIS" 
        self.expand=True
        self.size=18