#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-

class Point:
    x: 0
    y: 0
    color: (0, 0, 0, 0)

    def __init__(self, x: int, y: int, color: tuple = (0, 0, 0, 0)) -> None:
        """

        @param x:
        @param y:
        @param color:
        """
        self.x = x
        self.y = y
        self.color = color

    def __eq__(self, other) -> bool:
        """

        @param other:
        @return:
        """
        return self.x == other.x and self.y == other.y

