class Pad:
    x: int = None
    y: int = None
    size: int = 40
    color: tuple = (0, 100, 200, .9)

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
