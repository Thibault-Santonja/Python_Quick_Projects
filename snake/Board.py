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
        snake_head = Point.Point(
            self._rest + self._map_size//2 * self._block_size,
            self._rest + self._map_size//2 * self._block_size,
            color=config.SNAKE)
        self._snake = Snake.Snake(snake_head)

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
        pygame.display.update()

    def _calculate_position(self, move_x: int, move_y: int) -> Point.Point:
        """

        @param move_x:
        @param move_y:
        @return:
        """
        tail = None

        if self._food == self._snake.head:
            if not self._snake.eat(move_x, -move_y):
                self._continue = False
            self._create_food()
        else:
            tail = self._snake.move(move_x, -move_y)

            if not tail:
                self._continue = False

        if self._snake.head.x < self._rest or self._snake.head.x > self._block_size * self._map_size or \
                self._snake.head.y < self._rest or self._snake.head.y > self._block_size * self._map_size:
            self._continue = False


        return tail

    def _create_food(self):
        self._food = Point.Point(
            self._rest + random.randint(0, self._map_size-1) * self._block_size,
            self._rest + random.randint(0, self._map_size-1) * self._block_size,
            config.FOOD)
        pygame.draw.rect(self._screen, self._food.color,
                         [self._food.x, self._food.y, self._block_size, self._block_size])

    def _update_snake_position(self, move_x: int, move_y: int):
        """

        @param move_x:
        @param move_y:
        @return:
        """
        # Calculate new position
        old_tail_position = self._calculate_position(move_x, move_y)

        # Update head bloc
        pygame.draw.rect(self._screen, self._snake.head.color,
                         [self._snake.head.x, self._snake.head.y, self._block_size, self._block_size])

        if old_tail_position:
            # Delete old tail
            pygame.draw.rect(self._screen, config.BOARD,
                             [old_tail_position.x, old_tail_position.y, self._block_size, self._block_size])

    def _keyboard_action(self, event, move_x, move_y):
        """

        @param event:
        @param move_x:
        @param move_y:
        @return:
        """
        move_entry = False

        # Quit the UI
        if event.type == pygame.QUIT:
            self._continue = False

        if event.type == pygame.KEYDOWN:
            match event.key:
                # Move
                case pygame.K_LEFT:
                    if move_x >= 0:
                        move_x = -self._block_size
                        move_y = 0
                        move_entry = True
                case pygame.K_RIGHT:
                    if move_x >= 0:
                        move_x = self._block_size
                        move_y = 0
                        move_entry = True
                case pygame.K_UP:
                    if move_y >= 0:
                        move_x = 0
                        move_y = self._block_size
                        move_entry = True
                case pygame.K_DOWN:
                    if move_y >= 0:
                        move_x = 0
                        move_y = -self._block_size
                        move_entry = True
                # Quit the UI
                case pygame.K_ESCAPE:
                    self._continue = False
        return move_x, move_y, move_entry

    def _run(self) -> None:
        """

        @return:
        """
        self._draw_grid()
        self._create_food()

        move_x = 0
        move_y = 0

        while not self._continue:
            for event in pygame.event.get():
                move_x, move_y, _ = self._keyboard_action(event, move_x, move_y)
                if move_y + move_x != 0:
                    self._continue = True

        while self._continue:
            move_entry = False
            self._draw_grid()
            for event in pygame.event.get():
                # Get a keyboard action
                if not move_entry:
                    move_x, move_y, move_entry = self._keyboard_action(event, move_x, move_y)

            self._update_snake_position(move_x, move_y)

            # pygame.display.update()
            time.sleep(self._step_duration)

        pygame.quit()
