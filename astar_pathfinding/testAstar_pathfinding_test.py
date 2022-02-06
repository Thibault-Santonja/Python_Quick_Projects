from unittest import TestCase
import unittest

from astar_pathfinding import Case


class TestGrid(TestCase):
    pass


class CaseTest(unittest.TestCase):
    def testCase(self) -> None:
        case = Case.Case(row=1, col=1, width=1)
        self.assertEqual(case.get_pos(), (1, 1))

    def testGridIsEmpty(self, case: Case.Case = Case.Case(row=1, col=1, width=1)) -> None:
        self.assertEqual(case.is_obstacle(), False)
        self.assertEqual(case.is_visited(), False)
        self.assertEqual(case.is_to_visit(), False)
        self.assertEqual(case.is_start(), False)
        self.assertEqual(case.is_end(), False)

    def testCaseInit(self, case: Case.Case = Case.Case(row=1, col=1, width=1)) -> None:
        self.testGridIsEmpty(case)

    def testCaseVisited(self, case: Case.Case = Case.Case(row=1, col=1, width=1)) -> None:
        case.set_visited()
        self.assertEqual(case.is_obstacle(), False)
        self.assertEqual(case.is_visited(), True)
        self.assertEqual(case.is_to_visit(), False)
        self.assertEqual(case.is_start(), False)
        self.assertEqual(case.is_end(), False)

    def testCaseToVisit(self, case: Case.Case = Case.Case(row=1, col=1, width=1)) -> None:
        case.set_to_visit()
        self.assertEqual(case.is_obstacle(), False)
        self.assertEqual(case.is_visited(), False)
        self.assertEqual(case.is_to_visit(), True)
        self.assertEqual(case.is_start(), False)
        self.assertEqual(case.is_end(), False)

    def testCaseObstacle(self, case: Case.Case = Case.Case(row=1, col=1, width=1)) -> None:
        case.set_obstacle()
        self.assertEqual(case.is_obstacle(), True)
        self.assertEqual(case.is_visited(), False)
        self.assertEqual(case.is_to_visit(), False)
        self.assertEqual(case.is_start(), False)
        self.assertEqual(case.is_end(), False)

    def testCaseStart(self, case: Case.Case = Case.Case(row=1, col=1, width=1)) -> None:
        case.set_start()
        self.assertEqual(case.is_obstacle(), False)
        self.assertEqual(case.is_visited(), False)
        self.assertEqual(case.is_to_visit(), False)
        self.assertEqual(case.is_start(), True)
        self.assertEqual(case.is_end(), False)

    def testCaseEnd(self, case: Case.Case = Case.Case(row=1, col=1, width=1)) -> None:
        case.set_end()
        self.assertEqual(case.is_obstacle(), False)
        self.assertEqual(case.is_visited(), False)
        self.assertEqual(case.is_to_visit(), False)
        self.assertEqual(case.is_start(), False)
        self.assertEqual(case.is_end(), True)

    def testCaseReset(self, case: Case.Case = Case.Case(row=1, col=1, width=1)) -> None:
        case.reset()
        self.testGridIsEmpty(case)

    def testCaseDistance(self, case1: Case.Case = Case.Case(row=1, col=1, width=1),
                         case2: Case.Case = Case.Case(row=4, col=2, width=1)) -> None:
        self.assertEqual(case1.get_distance(case2), 4)
