class Brick:
    x: int = None
    y: int = None
    size_x: int = None
    size_y: int = None
    color: tuple = (214, 125, 62, .9)

    def __init__(self, x: int, y: int, size_x: int, size_y: int,):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
