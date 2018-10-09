#!/usr/bin/env python3
"""
Reverse a string (trivial in python) 
"""

__author__ = "Stick"
__license__ = "Unlicense"


import sys


def reverse(text):
    """ Reverse a string (trivial in python) """
    return text[::-1]


if __name__ == "__main__":
    print(reverse(sys.argv[1]))
