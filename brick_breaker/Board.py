from brick_breaker import Pad, Ball, Brick


class Board:
    height: int = 800
    width: int = 800
    color: tuple = (249, 228, 212)
    _bricks: list = None
    _pad: Pad.Pad = None
    _ball: Ball.Ball = None

    def __init__(self):
        pad_size = 80
        self._pad = Pad.Pad(x=(self.width + pad_size)//2, y=self.height//20, size=pad_size)
        self._ball = Ball.Ball(x=(self.width + pad_size)//2, y=self.height//20)
        self._init_bricks(8, 3)

    def _init_bricks(self, columns: int, layers: int):
        """

        @return:
        """
        self._bricks = []

        for layer in range(layers):
            for brick in range(columns):
                self._bricks.append(Brick.Brick(x=self.width//columns * columns + 5,
                                                y=self.height//layers * layer + 5,
                                                size_x=self.width//columns - 10,
                                                size_y=self.height//20))

    def launch(self):
        pass
