#!/usr/bin/env python3
"""
Calculate the moment when someone has lived for 10^9 seconds.
"""

__author__ = "Stick"
__license__ = "Unlicense"


from datetime import datetime, timedelta
from sys import argv


def add_gigasecond(birth_date):
    """ Calculate the moment when someone has lived for 10^9 seconds """
    return birth_date + timedelta(seconds=10 ** 9)


if __name__ == "__main__":
    print(add_gigasecond(datetime(int(argv[1]), int(argv[2]), int(argv[3]))))
