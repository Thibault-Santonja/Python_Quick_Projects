from unittest import TestCase

import pygame

from astar_pathfinding import Case, Grid, config


class TestCaseClass(TestCase):
    def test_get_pos(self):
        pass

    def test_is_visited(self):
        pass

    def test_is_to_visit(self):
        pass

    def test_is_obstacle(self):
        pass

    def test_is_start(self):
        pass

    def test_is_end(self):
        pass

    def test_reset(self):
        pass

    def test_set_visited(self):
        pass

    def test_set_to_visit(self):
        pass

    def test_set_obstacle(self):
        pass

    def test_set_start(self):
        pass

    def test_set_end(self):
        pass

    def test_set_path(self):
        tested_case = Case.Case(1, 1, 1)
        self.assertEqual(tested_case.color, config.WHITE)
        tested_case.set_path()
        self.assertEqual(tested_case.color, config.BLUE)

    def test_draw(self):
        tested_case = Case.Case(1, 1, 1)

        pygame.init()
        window = pygame.display.set_mode((100, 100))

        self.assertEqual(tested_case.draw(window), None)

        pygame.quit()

    def test_get_distance(self):
        pass

    def test_update_neighbors(self):
        window_width: int = 800
        nb_rows: int = 50
        pygame.init()
        window = pygame.display.set_mode((window_width, window_width))

        test_grid = Grid.Grid(nb_rows, window, window_width)
        test_grid._create_grid()
        tested_case = Case.Case(1, 1, 1)

        self.assertEqual(tested_case.update_neighbors(test_grid), None)
        pygame.quit()
