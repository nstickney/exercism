#!/usr/bin/env python3
"""
Command-line program to run sum_of_multiples and print the answer
"""

__author__ = "Stick"
__license__ = "Unlicense"


from sys import argv
from sum_of_multiples import sum_of_multiples as som


def main(number, divisors):
    """ Run the program """
    print(som(number, divisors))


def print_usage():
    """ Print a helpful usage message """
    print("Usage: python[3]", argv[0], "<limit> <divisor> [more divisors] ")
    exit(1)


if __name__ == "__main__":
    if len(argv) < 3 or not all(i.isdigit() for i in argv[1:]):
        print_usage()

main(int(float(argv[1])), [int(float(i)) for i in argv[2:]])
