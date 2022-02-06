#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-

from unittest import TestCase
from snake.Snake import Snake
from snake.Point import Point


class TestSnake(TestCase):
    """

    """
    def test_head(self) -> None:
        """

        @return:
        """
        snake = Snake(Point(0, 0), 1)
        self.assertEqual(snake.head, Point(0, 0))

    def test_lenght(self) -> None:
        """

        @return:
        """
        snake = Snake(Point(0, 0), 4)
        self.assertEqual(snake.length, 4)
        snake.eat(2, 2)
        self.assertEqual(snake.length, 5)

    def test_move(self) -> None:
        """

        @return:
        """
        snake = Snake(Point(0, 0), 1)
        self.assertEqual(snake.move(1, 1), Point(0, 0))
        self.assertEqual(snake.length, 1)

    def test_eat(self) -> None:
        """

        @return:
        """
        snake = Snake(Point(0, 0), 1)
        self.assertEqual(snake.eat(0, 1), True)
        self.assertEqual(snake.length, 2)
        self.assertEqual(snake.eat(0, 2), True)
        self.assertEqual(snake.length, 3)
        self.assertEqual(snake.eat(0, -3), False)
        self.assertEqual(snake.length, 3)

    def test__update_position(self) -> None:
        """

        @return:
        """
        snake = Snake(Point(0, 0), 1)
        snake.eat(1, 1)
        self.assertEqual(snake.length, 2)
        self.assertEqual(snake._update_position(0, 0), True)
        self.assertEqual(snake.length, 3)
        self.assertEqual(snake._update_position(0, 0), False)
        self.assertEqual(snake.length, 3)

    def test__control_self_eating(self) -> None:
        """

        @return:
        """
        snake = Snake(Point(0, 0), 1)
        snake.eat(1, 1)
        self.assertEqual(snake._control_self_eating(), False)
        snake.eat(0, 0)
        self.assertEqual(snake._control_self_eating(), True)
