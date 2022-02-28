from typing import Tuple


def fib(n: int) -> int:
    """
    Calculates the nth Fibonacci number

    @type n: int
    @param n: nth Fibonacci number
    @return:
    """
    res, _ = fast_fib(abs(n))
    if n < 0 and n % 2 == 0:
        return -res
    return res


def fast_fib(n: int) -> Tuple[int, int]:
    """
    Calculates the nth Fibonacci using fast doubling multiplication

    @type n: int
    @param n: nth Fibonacci number
    @return:
    """
    if n == 0:
        return 0, 1

    a, b = fast_fib(n // 2)
    c = a * (b * 2 - a)
    d = a ** 2 + b ** 2

    return (c, d) if n % 2 == 0 else (d, c + d)
