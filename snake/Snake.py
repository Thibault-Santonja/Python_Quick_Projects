#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-

import copy
from typing import Optional

from snake import Point


class Snake:
    _head = None
    _body = None

    def __init__(self, head: Point.Point, initial_length=3) -> None:
        """

        @type head: Point.Point
        """
        self._body = []
        for i in range(initial_length):
            self._body.append(Point.Point(head.x, head.y, head.color))
        self._head = head

    @property
    def head(self) -> Point.Point:
        """
        Getter for head property

        @return:
        """
        return self._head

    @property
    def length(self) -> int:
        """
        Getter for snake length

        @return:
        """
        return len(self._body)

    def move(self, delta_x: int, delta_y: int) -> Optional[Point.Point]:
        """
        Move the snake

        @param delta_y:
        @param delta_x:
        @type delta_y: Point.Point
        @type delta_x: Point.Point
        """
        if not self._update_position(delta_x, delta_y):
            return None
        return self._body.pop(0)

    def eat(self, delta_x: int, delta_y: int) -> bool:
        """
        Move the snake and eat

        @param delta_y:
        @param delta_x:
        @type delta_y: Point.Point
        @type delta_x: Point.Point
        """
        if not self._update_position(delta_x, delta_y):
            return False
        return True

    def _update_position(self, delta_x: int, delta_y: int) -> bool:
        """
        Change snake position

        @param delta_y:
        @param delta_x:
        @type delta_y: Point.Point
        @type delta_x: Point.Point
        """
        self._head.x += delta_x
        self._head.y += delta_y

        if self._is_self_eating():
            return False

        self._body.append(copy.copy(self.head))
        return True

    def _is_self_eating(self) -> bool:
        """
        Check if the snake eat itself

        @return:
        """
        for element in self._body[:-1]:
            if element == self._head:
                return True
        return False

    def is_overlap(self, point: Point.Point) -> bool:
        """
        Check if the snake eat itself

        @param point:
        @return:
        """
        for element in self._body:
            if element == point:
                return True
        return False
