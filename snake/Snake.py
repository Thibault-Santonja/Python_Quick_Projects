from snake import Point
import queue


class Snake:
    _head = None
    _body = queue.Queue()
    length = 1

    def __init__(self, head: Point.Point):
        """

        @type head: Point.Point
        """
        self._body.put(head)
        self._head = head

    @property
    def head(self) -> Point.Point:
        """

        @return:
        """
        return self._head

    def move(self, delta_x: int, delta_y: int) -> Point.Point:
        """

        @param delta_y:
        @param delta_x:
        @type delta_y: Point.Point
        @type delta_x: Point.Point
        """
        self._update_position(delta_x, delta_y)
        return self._body.get()

    def eat(self, delta_x: int, delta_y: int) -> None:
        """

        @param delta_y:
        @param delta_x:
        @type delta_y: Point.Point
        @type delta_x: Point.Point
        """
        self._update_position(delta_x, delta_y)

    def _update_position(self, delta_x: int, delta_y: int):
        """

        @param delta_y:
        @param delta_x:
        @type delta_y: Point.Point
        @type delta_x: Point.Point
        """
        self._head.x += delta_x
        self._head.y += delta_y

        self._body.put(self.head)
