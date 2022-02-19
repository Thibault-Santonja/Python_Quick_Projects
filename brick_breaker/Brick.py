class Brick:
    _x: int = None
    _y: int = None
    _size_x: int = None
    _size_y: int = None
    _color: tuple = (214, 125, 62, .9)

    def __init__(self, x: int, y: int, size_x: int, size_y: int,):
        self._x = x
        self._y = y
        self._size_x = size_x
        self._size_y = size_y

    def draw(self, pygame, screen):
        pygame.draw.rect(screen, self._color, [self._x, self._y, self._size_x, self._size_y])
