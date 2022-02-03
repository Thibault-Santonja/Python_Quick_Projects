from snake import Point
import queue


class Snake:
    head = None
    body = queue.Queue()
    length = 1

    def __init__(self, head: Point.Point):
        """

        @type head: Point.Point
        """
        self.body.put(head)
        self.head = head

    def update_position(self, head: Point.Point) -> Point.Point:
        """

        @type head: Point.Point
        """
        self.head = head
        self.body.put(head)
        return self.body.get()

    def upgrade_size(self, head: Point.Point) -> None:
        """

        @type head: Point.Point
        """
        self.head = head
        self.body.put(head)
