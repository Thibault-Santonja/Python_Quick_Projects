from unittest import TestCase
import unittest

import Case


class TestGrid(TestCase):
    pass


class CaseTest(unittest.TestCase):
    def run(self, **kwargs):
        print("\nRun all tests :")

        case1 = Case.Case(row=1, col=1, width=1)
        case2 = Case.Case(row=1, col=5, width=1)

        self.testCaseInit(case1)
        self.testCaseVisited(case1)
        self.testCaseToVisit(case1)
        self.testCaseObstacle(case1)
        self.testCaseStart(case1)
        self.testCaseEnd(case1)
        self.testCaseReset(case1)

        self.testCaseDistance(case1, case2)

        print("\nRun all test is finished !")

    def testCase(self):
        case1 = Case.Case(row=1, col=1, width=1)
        print(" - test fct()")

        self.assertEqual(case1.get_pos(), (1, 1))

    def testGridIsEmpty(self, case):
        self.assertEqual(case.is_obstacle(), False)
        self.assertEqual(case.is_visited(), False)
        self.assertEqual(case.is_to_visit(), False)
        self.assertEqual(case.is_start(), False)
        self.assertEqual(case.is_end(), False)

    def testCaseInit(self, case):
        print(" - test CaseInit()")
        self.testGridIsEmpty(case)

    def testCaseVisited(self, case):
        print(" - test CaseVisited()")
        case.set_visited()
        self.assertEqual(case.is_obstacle(), False)
        self.assertEqual(case.is_visited(), True)
        self.assertEqual(case.is_to_visit(), False)
        self.assertEqual(case.is_start(), False)
        self.assertEqual(case.is_end(), False)

    def testCaseToVisit(self, case):
        print(" - test CaseToVisit()")
        case.set_to_visit()
        self.assertEqual(case.is_obstacle(), False)
        self.assertEqual(case.is_visited(), False)
        self.assertEqual(case.is_to_visit(), True)
        self.assertEqual(case.is_start(), False)
        self.assertEqual(case.is_end(), False)

    def testCaseObstacle(self, case):
        print(" - test CaseObstacle()")
        case.set_obstacle()
        self.assertEqual(case.is_obstacle(), True)
        self.assertEqual(case.is_visited(), False)
        self.assertEqual(case.is_to_visit(), False)
        self.assertEqual(case.is_start(), False)
        self.assertEqual(case.is_end(), False)

    def testCaseStart(self, case):
        print(" - test CaseStart()")
        case.set_start()
        self.assertEqual(case.is_obstacle(), False)
        self.assertEqual(case.is_visited(), False)
        self.assertEqual(case.is_to_visit(), False)
        self.assertEqual(case.is_start(), True)
        self.assertEqual(case.is_end(), False)

    def testCaseEnd(self, case):
        print(" - test CaseEnd()")
        case.set_end()
        self.assertEqual(case.is_obstacle(), False)
        self.assertEqual(case.is_visited(), False)
        self.assertEqual(case.is_to_visit(), False)
        self.assertEqual(case.is_start(), False)
        self.assertEqual(case.is_end(), True)

    def testCaseReset(self, case):
        print(" - test CaseReset()")
        case.reset()
        self.testGridIsEmpty(case)

    def testCaseDistance(self, case1, case2):
        print(" - test CaseDistance()")

        self.assertEqual(case1.get_distance(case2), 4)
