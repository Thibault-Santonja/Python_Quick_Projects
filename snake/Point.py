class Point:
    x: 0
    y: 0
    color: (0, 0, 0, 0)

    def __init__(self, x: int, y: int, color: tuple = (0, 0, 0, 0)):
        self.x = x
        self.y = y
        self.color = color

    def move(self, delta_x: int, delta_y: int):
        self.x += delta_x
        self.y += delta_y

