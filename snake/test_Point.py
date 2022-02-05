from unittest import TestCase
from snake.Point import Point


class TestPoint(TestCase):
    def test_eq(self):
        self.assertEqual(Point(12, 12), Point(12, 12))
        self.assertNotEqual(Point(12, 0), Point(12, 12))
