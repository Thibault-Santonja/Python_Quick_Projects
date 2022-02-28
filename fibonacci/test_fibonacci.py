from unittest import TestCase

from fibonacci import fibonacci


class TestFibonacci(TestCase):
    def test_fib_base(self):
        self.assertEqual(fibonacci.fib(0), 0)
        self.assertEqual(fibonacci.fib(1), 1)
        self.assertEqual(fibonacci.fib(2), 1)
        self.assertEqual(fibonacci.fib(3), 2)
        self.assertEqual(fibonacci.fib(4), 3)
        self.assertEqual(fibonacci.fib(5), 5)

    def test_golden_ratio(self):
        golden_ratio = (1 + 5**(1/2)) / 2
        f1, _ = fibonacci.fast_fib(1001)
        f0, _ = fibonacci.fast_fib(1000)

        self.assertEqual(f1 / f0, golden_ratio)

    def test_fib_negative(self):
        self.assertEqual(fibonacci.fib(-6), -8)
        self.assertEqual(fibonacci.fib(-21), 10946)
        self.assertEqual(fibonacci.fib(-50), -12586269025)
        self.assertEqual(fibonacci.fib(-85), 259695496911122585)
        self.assertEqual(fibonacci.fib(-96), -51680708854858323072)
