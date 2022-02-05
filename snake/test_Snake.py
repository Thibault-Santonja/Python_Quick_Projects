from unittest import TestCase
from snake.Snake import Snake
from snake.Point import Point


class TestSnake(TestCase):
    def test_head(self):
        snake = Snake(Point(0, 0), 1)
        self.assertEqual(snake.head, Point(0, 0))

    def test_lenght(self):
        snake = Snake(Point(0, 0), 3)
        self.assertEqual(snake.lenght, 3)
        snake.eat(2, 2)
        self.assertEqual(snake.lenght, 4)

    def test_move(self):
        snake = Snake(Point(0, 0), 1)
        self.assertEqual(snake.move(1, 1), Point(0, 0))
        self.assertEqual(snake.lenght, 1)

    def test_eat(self):
        snake = Snake(Point(0, 0), 1)
        self.assertEqual(snake.eat(1, 1), False)
        self.assertEqual(snake.eat(0, 0), True)
        self.assertEqual(snake.lenght, 3)

    def test__update_position(self):
        snake = Snake(Point(0, 0), 1)
        snake.eat(1, 1)
        self.assertEqual(snake.lenght, 2)
        self.assertEqual(snake._update_position(0, 0), True)
        self.assertEqual(snake.lenght, 3)
        self.assertEqual(snake._update_position(0, 0), False)
        self.assertEqual(snake.lenght, 3)

    def test__control_self_eating(self):
        snake = Snake(Point(0, 0), 1)
        snake.eat(1, 1)
        self.assertEqual(snake._control_self_eating(), False)
        snake.eat(0, 0)
        self.assertEqual(snake._control_self_eating(), True)
