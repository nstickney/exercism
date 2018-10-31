#!/usr/bin/env python3
"""
Command-line program to run perfect_number and print the answer
"""

__author__ = "Stick"
__license__ = "Unlicense"


from sys import argv
from perfect_numbers import classify


def main(number):
    """ Run the program """
    print(classify(number))


def print_usage():
    """ Print a helpful usage message """
    print("Usage: python[3]", argv[0], "<number>")
    exit(1)


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print_usage()

    main(int(float(argv[1])))
