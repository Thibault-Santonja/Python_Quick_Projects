#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-

import time

import pygame
import random

from snake import Point
from snake import config
from snake import Snake


def _handle_left(move_x: int, move_y: int, bloc_size: int) -> tuple:
    """

    @param move_x:
    @param move_y:
    @return:
    """
    if move_x >= 0:
        return -bloc_size, 0, True
    return move_x, move_y, False


def _handle_right(move_x: int, move_y: int, bloc_size: int) -> tuple:
    """

    @param move_x:
    @param move_y:
    @return:
    """
    if move_x >= 0:
        return bloc_size, 0, True
    return move_x, move_y, False


def _handle_up(move_x: int, move_y: int, bloc_size: int) -> tuple:
    """

    @param move_x:
    @param move_y:
    @return:
    """
    if move_y >= 0:
        return 0, bloc_size, True
    return move_x, move_y, False


def _handle_down(move_x: int, move_y: int, bloc_size: int) -> tuple:
    """

    @param move_x:
    @param move_y:
    @return:
    """
    if move_y >= 0:
        return 0, -bloc_size, True
    return move_x, move_y, False


def _handle_escape(move_x: int, move_y: int, _) -> tuple:
    """

    @param move_x:
    @param move_y:
    @return:
    """
    pygame.quit()
    return move_x, move_y, False


KEYBOARD_EVENT = {
    pygame.K_LEFT: _handle_left,
    pygame.K_RIGHT: _handle_right,
    pygame.K_UP: _handle_up,
    pygame.K_DOWN: _handle_down,
    pygame.K_ESCAPE: _handle_escape
}


class Board:
    """
    _screen: Screen size in pixels
    _continue: Boolean to stop the game
    _block_size: Size of square in pixels
    _map_size: number of blocb per line and column
    _step_duration: Time in second between each movement
    _rest: rest of the division between map size and screen size
    _snake: store the Snake instance
    _food: store a Point instance to locate the food
    _score_font: Store the font of the UI
    _initial_length: Initial snake size

    """
    _screen = 800
    _continue = False
    _block_size = 20
    _map_size = 30
    _step_duration = .1
    _rest = 0
    _snake = None
    _food = None
    _score_font = None
    _initial_length = 3

    def __init__(self, window_width: int = 800, map_size: int = 30, initial_length: int = 3) -> None:
        """

        @type initial_length: int
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
        self.initial_length = initial_length
        self._snake = Snake.Snake(snake_head, self.initial_length)

    def _init_screen(self) -> None:
        """
        Initialize the PyGame screen.
        """
        pygame.init()
        self._screen = pygame.display.set_mode((self._window_width, self._window_width))
        pygame.display.set_caption('Snake Game')
        self._screen.fill(config.BOARD)
        self._score_font = pygame.font.SysFont('dejavusans', 32)

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
        Verify if snake head touch a food or a border

        @param move_x:
        @param move_y:
        @type move_x: int
        @type move_y: int
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

    def _create_food(self) -> None:
        """
        Generate a piece of food

        @return:
        """
        food_created = False
        while not food_created:
            self._food = Point.Point(
                self._rest + random.randint(0, self._map_size-1) * self._block_size,
                self._rest + random.randint(0, self._map_size-1) * self._block_size,
                config.FOOD)
            if not self._snake.is_overlap(self._food):
                food_created = True
                pygame.draw.rect(self._screen, self._food.color,
                                 [self._food.x, self._food.y, self._block_size, self._block_size])

    def _update_snake_position(self, move_x: int, move_y: int) -> None:
        """
        Update UI for snake position

        @param move_x:
        @param move_y:
        @type move_x: int
        @type move_y: int
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

    def _keyboard_action(self, event, move_x: int, move_y: int) -> (int, int, bool):
        """
        Get keyboard action

        @param event:
        @param move_x:
        @param move_y:
        @type move_x: int
        @type move_y: int
        @return:
        """
        # fixme : to log on DEBUG mode `print(event)`
        move_entry = False

        # Quit the UI
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            event_handler = KEYBOARD_EVENT.get(event.key)
            move_x, move_y, move_entry = event_handler(move_x, move_y, self._block_size)

        return move_x, move_y, move_entry

    def _start_game(self, move_x: int, move_y: int) -> (int, int):
        """
        Begining of the game, waiting for start

        @param move_x:
        @param move_y:
        @type move_x: int
        @type move_y: int
        @return:
        """
        while not self._continue:
            for event in pygame.event.get():
                move_x, move_y, _ = self._keyboard_action(event, move_x, move_y)
                if move_y + move_x != 0:
                    self._continue = True

        return move_x, move_y

    def _score(self, score: int) -> None:
        """
        display score

        @param score:
        @type score: int
        @return:
        """
        self._screen.blit(self._score_font.render(f"Your Score: {score-1}", True, config.BOARD), [0, 0])
        self._screen.blit(self._score_font.render(f"Your Score: {score}", True, config.SNAKE), [0, 0])

    def _game_over(self) -> None:
        """
        managed end game

        @return:
        """
        self._screen.blit(self._score_font.render("Game Over !", True, config.SNAKE),
                          [self._map_size * self._block_size//2, self._map_size * self._block_size//2])
        self._draw_grid()
        stop = False
        while not stop:
            for event in pygame.event.get():
                # Quit the UI
                if event.type == pygame.QUIT:
                    pygame.quit()
                    stop = True
                if event.type == pygame.KEYDOWN and pygame.K_ESCAPE:
                    pygame.quit()
                    stop = True

    def run(self) -> None:
        """
        Run the game

        @return:
        """
        self._init_screen()
        self._draw_grid()

        self._create_food()
        move_x, move_y = self._start_game(0, 0)

        while self._continue:
            move_entry = False
            self._draw_grid()
            for event in pygame.event.get():
                # Get a keyboard action
                if not move_entry:
                    move_x, move_y, move_entry = self._keyboard_action(event, move_x, move_y)

            self._update_snake_position(move_x, move_y)
            self._score(self._snake.length - self.initial_length)

            # pygame.display.update()
            time.sleep(self._step_duration)

        self._game_over()
