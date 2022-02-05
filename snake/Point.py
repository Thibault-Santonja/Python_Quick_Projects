class Point:
    x: 0
    y: 0
    color: (0, 0, 0, 0)

    def __init__(self, x: int, y: int, color: tuple = (0, 0, 0, 0)):
        self.x = x
        self.y = y
        self.color = color

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

