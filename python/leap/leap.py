#!/usr/bin/env python3
"""
Determine whether a year is a leap year or not
"""

__author__ = "Stick"
__version__ = "0.1.0"
__license__ = "Unlicense"


import sys


def is_leap_year(year):
    """ Determine whether a year is a leap year or not """
    return (year % 400 == 0) or (year % 4 == 0 and not year % 100 == 0)


if __name__ == "__main__":
    print(sys.argv[1], is_leap_year(int(sys.argv[1])))
