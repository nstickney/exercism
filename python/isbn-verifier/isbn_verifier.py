#!/usr/bin/env python3
"""
Determine whether a given ISBN is valid or not
"""

__author__ = "Stick"
__license__ = "Unlicense"


from sys import argv


def verify(isbn):

    # Prepare
    isbn = isbn.replace("-", "")

    # Trivial check
    if len(isbn) != 10:
        return False

    # Parse the string
    total = 0
    for i, d in enumerate(isbn):
        if d.isdigit():
            total += int(d) * (10 - i)
        elif d.upper() == "X" and i == 9:
            total += 10
        else:
            return False

    return total % 11 == 0


def main(isbn):
    print(verify(isbn))


def print_usage():
    print("Usage: python[3]", argv[0], "<isbn>")
    print("    isbn:  isbn to verify")
    exit(1)


if __name__ == "__main__":
    if len(argv) != 2:
        print_usage()
    main(argv[1])
