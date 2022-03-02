from unittest import TestCase


from google_code_jam import wires


class Test(TestCase):
    def test_calculate_intersections_basic(self):
        self.assertEqual(wires.calculate_intersections([]), 0)
        self.assertEqual(wires.calculate_intersections([(1, 1)]), 0)
        self.assertEqual(wires.calculate_intersections([(1, 1), (2, 3)]), 0)
        self.assertEqual(wires.calculate_intersections([(1, 0), (2, 2)]), 0)

    def test_calculate_intersections_parallax(self):
        self.assertEqual(wires.calculate_intersections([(1, 1), (2, 2), (3, 3)]), 0)
        self.assertEqual(wires.calculate_intersections([(1, 2), (2, 3), (3, 4)]), 0)
        self.assertEqual(wires.calculate_intersections([(1, 0), (2, 1), (3, 2)]), 0)

    def test_calculate_intersections_increase(self):
        self.assertEqual(wires.calculate_intersections([(1, 4), (2, 2), (3, 3)]), 2)
        self.assertEqual(wires.calculate_intersections([(1, 5), (2, 3), (3, 4)]), 2)
        self.assertEqual(wires.calculate_intersections([(1, 3), (2, 1), (3, 2)]), 2)

    def test_calculate_intersections_decrease(self):
        self.assertEqual(wires.calculate_intersections([(4, 1), (2, 2), (3, 3)]), 2)
        self.assertEqual(wires.calculate_intersections([(4, 2), (2, 3), (3, 4)]), 2)
        self.assertEqual(wires.calculate_intersections([(4, 0), (2, 1), (3, 2)]), 2)

    # Fixme: hard intersection (on a same point)
    def test_calculate_intersections_intersect_hard(self):
        self.assertEqual(wires.calculate_intersections([(1, 3), (2, 2), (3, 1)]), 1)
        self.assertEqual(wires.calculate_intersections([(1, 4), (2, 3), (4, 1)]), 1)
        self.assertEqual(wires.calculate_intersections([(1, 4), (3, 2), (4, 1)]), 1)

    def test_calculate_intersections_intersect_simple(self):
        self.assertEqual(wires.calculate_intersections([(1, 5), (2, 2), (5, 1)]), 3)
        self.assertEqual(wires.calculate_intersections([(1, 5), (2, 3), (5, 1)]), 3)
        self.assertEqual(wires.calculate_intersections([(1, 5), (3, 2), (5, 1)]), 3)

    def test_calculate_intersections_negative(self):
        self.assertEqual(wires.calculate_intersections([(-1, -1)]), 0)
        self.assertEqual(wires.calculate_intersections([(-1, -1), (-2, -3)]), 0)
        self.assertEqual(wires.calculate_intersections([(-1, 0), (-2, -2)]), 0)
        self.assertEqual(wires.calculate_intersections([(-1, 0), (-2, -1), (-3, -2)]), 0)
        self.assertEqual(wires.calculate_intersections([(-1, -4), (-2, -2), (-3, -3)]), 2)
        self.assertEqual(wires.calculate_intersections([(-4, -1), (-2, -2), (-3, -3)]), 2)

    def test_calculate_intersections_positive_negative(self):
        self.assertEqual(wires.calculate_intersections([(-1, 1)]), 0)
        self.assertEqual(wires.calculate_intersections([(-1, 1), (-2, -3)]), 0)
        self.assertEqual(wires.calculate_intersections([(1, 0), (-2, -2)]), 0)
        self.assertEqual(wires.calculate_intersections([(1, 0), (2, 1), (-3, -2)]), 0)
        self.assertEqual(wires.calculate_intersections([(-4, 4), (-2, -2), (3, 3)]), 2)
        self.assertEqual(wires.calculate_intersections([(4, -4), (-2, -2), (3, 3)]), 2)

    def test_find_line_intersection_point(self):
        self.assertEqual(wires.find_line_intersection_point(
            (0, 1),
            (2, 3),
            (0, 2),
            (2, 2),
        ), (1, 2))
        with self.assertRaises(ValueError):
            wires.find_line_intersection_point(
                (0, 1),
                (2, 3),
                (0, 1),
                (2, 3),
            )

    def test_det(self):
        self.assertEqual(wires.det((1, 3), (2, 2)), -4)
