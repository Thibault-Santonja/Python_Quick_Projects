#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-

import time
import pygame

from brick_breaker import keyboard, config


def trigger_game_over() -> None:
    # Todo : to update to replay the game
    time.sleep(1)
    pygame.quit()


class Board:
    _height: int = 600
    _width: int = 800
    _color: tuple = config.COLORS["BOARD"]
    _bricks: list = None
    _bricks_columns: int = 8
    _bricks_layers: int = 5
    _pad: pygame.Rect = None
    _ball: pygame.Rect = None
    _ball_direction: list = [1, -1]
    _screen: pygame.Surface = None
    _score_font: pygame.font.Font = None
    _score: int = 0

    def __init__(self) -> None:
        # Init screen and draw it
        self._init_screen()
        self._init_bricks()
        self._init_pad()
        self._init_ball()

    def __del__(self) -> None:
        pygame.quit()

    def _init_screen(self) -> None:
        """
        Initialize the PyGame screen.
        """
        pygame.init()
        self._screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption('Brick Breaker Game')
        self._screen.fill(self._color)
        self._score_font = pygame.font.SysFont('dejavusans', 32)
        pygame.display.update()

    def _init_bricks(self, screen_layer_proportion: float = .40, block_gap: int = 2) -> None:
        """

        @type screen_layer_proportion: float
        @param screen_layer_proportion: percentage of screen covered by bricks. (By default 40 %)
        @type block_gap: int
        @param block_gap:
        @return:
        """
        self._bricks = []

        for layer in range(self._bricks_layers):
            for col in range(self._bricks_columns):
                x = self._width // self._bricks_columns * col + block_gap
                y = int(self._height / (self._bricks_layers * 1/screen_layer_proportion) * layer + block_gap)
                size_x = self._width // self._bricks_columns - block_gap * 2
                size_y = int(self._height / (self._bricks_layers * 1/screen_layer_proportion) - block_gap * 2)

                brick = pygame.Rect(x, y, size_x, size_y)
                self._draw(config.COLORS["BRICK"], brick)
                self._bricks.append(brick)

    def _init_pad(self) -> None:
        pad_size = self._width // 6
        x = (self._width - pad_size) // 2
        y = self._height - 20

        self._pad = pygame.Rect(x, y, pad_size, 10)
        self._draw(config.COLORS["PAD"], self._pad)

    def _init_ball(self) -> None:
        ball_size = 5
        x = self._width // 2
        y = self._height - 25

        self._ball = pygame.Rect(x, y, ball_size, ball_size)
        self._draw(config.COLORS["BALL"], self._ball)

    def _draw(self, color: tuple, rect: pygame.Rect) -> None:
        pygame.draw.rect(self._screen, color, rect)

    def _update_pad_position(self, delta_x: int) -> None:
        if (delta_x < 0 <= self._pad.x) or (self._pad.x + self._pad.width <= self._width and delta_x > 0):
            # Erase pad
            self._draw(config.COLORS["BOARD"], self._pad)

            # Calculate new position
            self._pad.update(
                self._pad.x + delta_x * self._width // 50,
                self._pad.y,
                self._pad.width,
                self._pad.height
            )

            # Redraw it
            self._draw(config.COLORS["PAD"], self._pad)

    def _check_wall_ball_overlap(self) -> None:
        if 0 >= self._ball.x or self._ball.x >= self._width:
            self._ball_direction[0] *= -1

        # 0 >= self._y or self._y >= screen_height
        if 0 >= self._ball.y or self._ball.y >= self._height:
            self._ball_direction[1] *= -1

    def _check_wall_brick_overlap(self) -> None:
        brick_overlapped = self._ball.collidelist(self._bricks)

        if brick_overlapped >= 0:
            self._draw(config.COLORS["BOARD"], self._bricks[brick_overlapped])
            self._bricks.remove(self._bricks[brick_overlapped])
            self._ball_direction[1] *= -1
            self._score += 1

    def _check_wall_pad_overlap(self) -> None:
        if self._ball.colliderect(self._pad):
            self._ball_direction[1] *= -1

    def _update_ball_position(self, delta: int) -> bool:
        # Erase
        self._draw(config.COLORS["BOARD"], self._ball)

        # update position
        self._ball.x += delta * self._ball_direction[0]
        self._ball.y += delta * self._ball_direction[1]

        # Overlap controls
        self._check_wall_ball_overlap()
        self._check_wall_brick_overlap()
        self._check_wall_pad_overlap()

        # Redraw
        self._draw(config.COLORS["BALL"], self._ball)

        # Control victory conditions
        if self._height <= self._ball.y:
            return False
        return True

    def _update_board(self, pad_horizontal_movement: int) -> bool:
        continue_game = True

        self._update_pad_position(pad_horizontal_movement)
        if not self._update_ball_position(self._width // 200):
            continue_game = False

        pygame.display.update()
        return continue_game

    def launch(self) -> None:
        continue_game = True
        horizontal_movement = 0

        while continue_game:
            time.sleep(1/60)  # 60 fps

            for event in pygame.event.get():
                res = keyboard.get_keyboard_action(event)
                if continue_game and res:
                    _, horizontal_movement = res
                else:
                    continue_game = False

            if continue_game:
                continue_game = self._update_board(horizontal_movement)

            if continue_game and not self._bricks:
                continue_game = False
                # Todo : Print GG message
                return trigger_game_over()

        # Todo : Print Game Over message
        return trigger_game_over()
