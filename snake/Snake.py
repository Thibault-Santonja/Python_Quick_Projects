import copy
from typing import Optional

from snake import Point


class Snake:
    _head = None
    _body = []

    def __init__(self, head: Point.Point, size=3):
        """

        @type head: Point.Point
        """
        for i in range(size):
            self._body.append(Point.Point(head.x, head.y, head.color))
        self._head = head

    @property
    def head(self) -> Point.Point:
        """

        @return:
        """
        return self._head

    @property
    def lenght(self) -> int:
        """

        @return:
        """
        return len(self._body)

    def move(self, delta_x: int, delta_y: int) -> Optional[Point.Point]:
        """

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

        @param delta_y:
        @param delta_x:
        @type delta_y: Point.Point
        @type delta_x: Point.Point
        """
        self._head.x += delta_x
        self._head.y += delta_y

        if self._controll_self_eating():
            return False

        self._body.append(copy.copy(self.head))
        return True

    def _controll_self_eating(self) -> bool:
        """

        @return:
        """
        for element in self._body[:-1]:
            if element == self._head:
                return True
        return False
