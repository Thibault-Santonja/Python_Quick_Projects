import time

import pygame
import config
import random


class Board:
    _screen = 800
    _continue = False
    _block_size = 20
    _map_size = 30
    _step_duration = .5
    _rest = 0

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

    def _run(self) -> None:
        self._continue = True

        move_x = 0
        move_y = 0

        snake_position_x = self._rest + self._map_size//2 * self._block_size
        snake_position_y = self._rest + self._map_size//2 * self._block_size

        while self._continue:
            for event in pygame.event.get():

                # Quit the UI
                if event.type == pygame.QUIT:
                    self._continue = False

                # Get a keyboard action
                if event.type == pygame.KEYDOWN:
                    # Move
                    match event.key:
                        case pygame.K_LEFT:
                            move_x = -self._block_size
                            move_y = 0
                        case pygame.K_RIGHT:
                            move_x = self._block_size
                            move_y = 0
                        case pygame.K_UP:
                            move_x = 0
                            move_y = self._block_size
                        case pygame.K_DOWN:
                            move_x = 0
                            move_y = -self._block_size
                        case pygame.K_ESCAPE: # Quit the UI
                            self._continue = False

            snake_position_x += move_x
            snake_position_y -= move_y
            pygame.draw.rect(self._screen, config.SNAKE,
                             [snake_position_x, snake_position_y, self._block_size, self._block_size])

            pygame.display.update()
            time.sleep(self._step_duration)

        pygame.quit()
