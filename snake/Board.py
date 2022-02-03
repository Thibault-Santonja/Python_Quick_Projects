import time

import pygame
import config
import random

from snake import Point
from snake import Snake


class Board:
    _screen = 800
    _continue = False
    _block_size = 20
    _map_size = 30
    _step_duration = .1
    _rest = 0
    _snake = None
    _food = None

    def __init__(self, window_width: int = 800, map_size: int = 30) -> None:
        """

        @type map_size: int
        @type window_width: int
        """
        # Initialize attributes
        self._window_width = window_width
        self._map_size = map_size
        self._block_size = self._window_width//map_size
        self._rest = (self._window_width % self._map_size) // 2
        self._snake = Point.Point(
            self._rest + self._map_size//2 * self._block_size,
            self._rest + self._map_size//2 * self._block_size,
            color=config.SNAKE)

        # Initialize the board and run the game
        self._init_screen()
        self._run()

    def _init_screen(self) -> None:
        """
        Initialize the PyGame screen.
        """
        pygame.init()
        self._screen = pygame.display.set_mode((self._window_width, self._window_width))
        self._screen.fill(config.BOARD)

    def _draw_grid(self):
        """
        Draw the grid on the PyGame screen
        """
        grid_size = self._block_size * self._map_size

        for id_x, x in enumerate(range(self._rest, grid_size, self._block_size)):
            for id_y, y in enumerate(range(self._rest, grid_size, self._block_size)):
                rect = pygame.Rect(x, y, self._block_size, self._block_size)
                pygame.draw.rect(self._screen, config.GRID, rect, 1)

    def _calculate_position(self, move_x: int, move_y: int):
        """

        @param move_x:
        @param move_y:
        @return:
        """
        self._snake.move(move_x, -move_y)

        if self._snake.x < self._rest or self._snake.x > self._block_size * self._map_size or \
                self._snake.y < self._rest or self._snake.y > self._block_size * self._map_size:
            self._continue = False

    def _run(self) -> None:
        """

        @return:
        """
        self._continue = True

        self._food = Point.Point(
            random.randint(0, self._map_size),
            random.randint(0, self._map_size),
            config.FOOD)

        move_x = 0
        move_y = 0

        while self._continue:
            self._draw_grid()
            for event in pygame.event.get():

                # Quit the UI
                if event.type == pygame.QUIT:
                    self._continue = False

                # Get a keyboard action
                if event.type == pygame.KEYDOWN:
                    match event.key:
                        # Move
                        case pygame.K_LEFT:
                            if move_x > 0:
                                continue
                            move_x = -self._block_size
                            move_y = 0
                        case pygame.K_RIGHT:
                            if move_x < 0:
                                continue
                            move_x = self._block_size
                            move_y = 0
                        case pygame.K_UP:
                            if move_y < 0:
                                continue
                            move_x = 0
                            move_y = self._block_size
                        case pygame.K_DOWN:
                            if move_y > 0:
                                continue
                            move_x = 0
                            move_y = -self._block_size
                        # Quit the UI
                        case pygame.K_ESCAPE:
                            self._continue = False

            self._calculate_position(move_x, move_y)
            pygame.draw.rect(self._screen, config.SNAKE,
                             [self._snake.x, self._snake.y, self._block_size, self._block_size])


            pygame.display.update()
            time.sleep(self._step_duration)

        pygame.quit()
