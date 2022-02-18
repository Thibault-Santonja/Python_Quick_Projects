class Pad:
    x: int = None
    y: int = None
    size: int = 40
    color: tuple = (71, 13, 33, .9)

    def __init__(self, x: int, y: int, size: int = 40):
        self.x = x
        self.y = y
        self.size = size
