#!/usr/bin/env python3
"""
Given a string of digits, calculate the largest product for a contiguous
substring of digits of length n.
"""

__author__ = "Stick"
__license__ = "Unlicense"


from sys import argv


def str_product(string):
    """ Calculate the product of all digits in a string """
    product = 1
    for i in string:
        product *= int(i)
    return product


def largest_product(digits, length):
    """ Calculate the largest product for contiguous substring of n digits """

    length = int(length)
    if length > len(digits):
        raise ValueError("Substring cannot be longer than string")

    if length < 0:
        raise ValueError("Substring length cannot be negative")

    return max([str_product(digits[x:x + length])
                for x in range(len(digits) - length + 1)])


def main(digits, length):
    """ Print the largest product for contiguous substring of n digits """
    print(largest_product(digits, length))


def print_usage():
    """ Print a helpful usage message """
    print("Usage: python[3]", argv[0], "<digits> <length>")
    exit(1)


if __name__ == "__main__":
    if len(argv) != 3 or (not argv[i].isdigit() for i in [1, 2]):
        print_usage()
    main(argv[1], argv[2])
