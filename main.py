#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "mprodhan"


def add(x, y):
    """Add two integers. Handles negative values."""
    return x + y


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    counter = 0
    if y < 0:
        for num in range(abs(y)):
            counter = add(-x, counter)
    for num in range(y):
        counter = add(x, counter)
    return counter


def power(x, n):
    """Raise x to power n, where n >= 0"""
    counter = 1
    for _num_ in range(n):
        counter = multiply(x, counter)
    return counter


def factorial(x):
    """Compute factorial of x, where x > 0"""
    counter = 1
    for e in range(2, add(x,1)):
        counter = multiply(counter, e)
    return counter


def fibonacci(n):
    a, b = 0, 1
    for fib in range(1, n):
        a, b = b, add(a, b)
    return b


# if __name__ == '__main__':
#     # your code to call functions above
#     pass
