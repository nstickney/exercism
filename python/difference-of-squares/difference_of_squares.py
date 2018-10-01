#!/usr/bin/env python3
"""
Find the difference between the square of the sum and the sum of the squares of
the first n natural numbers.
"""

__author__ = "Stick"
__version__ = "0.1.0"
__license__ = "Unlicense"


import sys


def square_of_sum(n):
    """ Calculate the square of the sum of the first n natural numbers """
    return sum(i for i in range(1, n + 1)) ** 2


def sum_of_squares(n):
    """ Calculate the sum of the squares of the first n natural numbers """
    return sum(i ** 2 for i in range(1, n + 1))


def difference(n):
    """ Find the difference between the square of the sum and the sum of the
    squares of the first n natural numbers"""
    return square_of_sum(n) - sum_of_squares(n)


if __name__ == "__main__":
    print(difference(abs(int(sys.argv[1]))))
