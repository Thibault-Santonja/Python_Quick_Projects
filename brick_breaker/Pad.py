from brick_breaker import config


class Pad:
    _x: int = None
    _y: int = None
    _size: int = 40
    _color: tuple = config.COLORS["PAD"]

    def __init__(self, x: int, y: int, size: int = 40):
        self._x = x
        self._y = y
        self._size = size

    def draw(self, pygame, screen):
        pygame.draw.rect(screen, self._color, [self._x, self._y, self._size, 20])

    def erase(self,pygame, screen):
        pygame.draw.rect(screen, config.COLORS["BOARD"], [self._x, self._y, self._size, 20])

    def update_position(self, delta_x, pygame, screen):
        self.erase(pygame, screen)
        self._x += delta_x
        self.draw(pygame, screen)
