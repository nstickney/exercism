#!/usr/bin/env python3
"""
Calculate the number of grains of wheat on a chessboard given that the number
on each square doubles.
"""

__author__ = "Stick"
__license__ = "Unlicense"


from sys import argv


def sanity_check(integer_number):
    """ Ensure the square is numbered 1-64 inclusive """
    if not 0 < integer_number < 65:
        raise ValueError("Square must be greater than 0 and less than 65")


def on_square(integer_number):
    """ Calculate the number of grains on this square """
    sanity_check(integer_number)
    # return 2 ** (integer_number - 1)
    return 1 << integer_number - 1


def total_after(integer_number):
    """ Calculate the total number of grains on the board """
    sanity_check(integer_number)
    # return sum(on_square(x + 1) for x in range(integer_number))
    return (1 << integer_number) - 1


def main(integer_number):
    """ Calculate the number of grains of wheat laid out on a chessboard """
    print("On square " + integer_number + ": " +
          str(on_square(int(integer_number))) + " grains")
    print("Total: " + str(total_after(int(integer_number))) + " grains")


def print_usage():
    """ Print a helpful usage message """
    print("Usage: python[3]", argv[0], "<square>")
    exit(1)


if __name__ == "__main__":
    if len(argv) != 2:
        print_usage()
    main(argv[1])
