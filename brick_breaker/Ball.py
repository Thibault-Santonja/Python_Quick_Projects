from brick_breaker import config


class Ball:
    _x: int = None
    _y: int = None
    _size: int = 5
    _color: tuple = config.COLORS["BALL"]

    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def draw(self, pygame, screen):
        pygame.draw.circle(screen, self._color, (self._x, self._y), self._size)
