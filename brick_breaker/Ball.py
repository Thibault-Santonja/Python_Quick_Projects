class Ball:
    x: int = None
    y: int = None
    size: int = 2
    color: tuple = (156, 15, 72, .9)

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y