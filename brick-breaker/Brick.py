class Brick:
    x: int = None
    y: int = None
    color: tuple = None

    def __init__(self, x: int, y: int, color: tuple):
        self.x = x
        self.y = y
        self.color = color
