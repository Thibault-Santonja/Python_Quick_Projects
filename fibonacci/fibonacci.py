"""
def fib(n):
    ""Calculates the nth Fibonacci number""
    res, _ = fast_fib(abs(n))
    return res if n > 0 else res * (-1)**(n+1)
"""


def fib(n):
    """Calculates the nth Fibonacci number"""
    res, _ = fast_fib(abs(n))
    if n < 0 and n % 2 == 0:
        return -res
    return res


def fast_fib(n: int):
    if n == 0:
        return 0, 1

    a, b = fast_fib(n // 2)
    c = a * (b * 2 - a)
    d = a ** 2 + b ** 2

    return (c, d) if n % 2 == 0 else (d, c + d)
