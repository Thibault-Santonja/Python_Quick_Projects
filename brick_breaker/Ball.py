from brick_breaker import config


class Ball:
    _x: int = None
    _y: int = None
    _x_sign: int = 1
    _y_sign: int = -1
    _size: int = 5
    _color: tuple = config.COLORS["BALL"]

    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def draw(self, pygame, screen):
        pygame.draw.circle(screen, self._color, (self._x, self._y), self._size)

    def erase(self, pygame, screen):
        pygame.draw.circle(screen, config.COLORS["BOARD"], (self._x, self._y), self._size)

    def check_wall(self, screen_width, screen_height):
        if 0 >= self._x or self._x >= screen_width:
            self._x_sign *= -1

        # 0 >= self._y or self._y >= screen_height
        if 0 >= self._y or self._y >= screen_height:
            self._y_sign *= -1

    def check_loose(self, screen_height) -> bool:
        if screen_height <= self._y:
            return True
        return False

    def update_position(self, delta, screen_width, screen_height, pygame, screen) -> bool:
        self.erase(pygame, screen)

        self._x += delta * self._x_sign
        self._y += delta * self._y_sign

        self.check_wall(screen_width, screen_height)

        self.draw(pygame, screen)

        if self.check_loose(screen_height):
            return False
        return True
