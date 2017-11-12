from problem2 import *


def example():
    return [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def test_fibonacci_exist():
    assert(fibonacci(1))


def test_fibo():
    assert(fibonacci(10) == example()) 