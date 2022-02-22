#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-

import time
import pygame

from brick_breaker import Pad, Ball, Brick, keyboard, config


class Board:
    _height: int = 600
    _width: int = 800
    _color: tuple = config.COLORS["BOARD"]
    _bricks: list = None
    _bricks_columns: int = 8
    _bricks_layers: int = 5
    _pad: Pad.Pad = None
    _ball: Ball.Ball = None
    _screen: pygame.Surface = None
    _score_font: pygame.font.Font = None

    def __init__(self):
        pad_size = 80
        self._pad = Pad.Pad(x=(self._width + pad_size) // 2, y=self._height // 20, size=pad_size)
        self._ball = Ball.Ball(x=(self._width + pad_size) // 2, y=self._height // 20)

    def __del__(self):
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

    def _init_bricks(self, screen_layer_proportion: float = .40, block_gap: int = 2):
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
                brick = Brick.Brick(x=self._width // self._bricks_columns * col + block_gap,
                                    y=int(self._height / (
                                            self._bricks_layers * 1/screen_layer_proportion) * layer + block_gap),
                                    size_x=self._width // self._bricks_columns - block_gap * 2,
                                    size_y=int(self._height / (
                                                self._bricks_layers * 1/screen_layer_proportion) - block_gap * 2))
                brick.draw(pygame, self._screen)
                self._bricks.append(brick)

    def _init_pad(self):
        pad_size = self._width // 6
        self._pad = Pad.Pad(x=(self._width - pad_size)//2, y=self._height-20, size=pad_size)
        self._pad.draw(pygame, self._screen)

    def _init_ball(self):
        self._ball = Ball.Ball(x=self._width//2, y=self._height-25)
        self._ball.draw(pygame, self._screen)

    def _init_game(self):
        # Init screen and draw it
        self._init_screen()
        self._init_bricks()
        self._init_pad()
        self._init_ball()

    def launch(self):
        self._init_game()
        continue_game = True
        horizontal_movement = 0

        while continue_game:
            time.sleep(1/60)  # 60 fps

            for event in pygame.event.get():
                res = keyboard.get_keyboard_action(event)
                print(res)
                if res:
                    _, horizontal_movement = res
                else:
                    continue_game = False
            self._pad.update_position(horizontal_movement * self._width // 50, self._width, pygame, self._screen)
            pygame.display.update()

        print("See you !")
        time.sleep(1)
        pygame.quit()
