#!/usr/bin/env python3
"""
Command-line program to determine what plants belong to which children
"""

__author__ = "Stick"
__license__ = "Unlicense"


from sys import argv
from kindergarten_garden import Garden


def main(garden, student):
    """ Run the program """
    print(garden.plants(student))


def print_usage():
    """ Print a helpful usage message """
    print("Usage: python[3]", argv[0], "<row1> <row2> [students] <query>")
    exit(1)


if __name__ == "__main__":
    if len(argv) < 4:
        print_usage()

    students = argv[3:-1]
    if students == []:
        students = None

    main(Garden(argv[1] + "\n" + argv[2], students), argv[-1])
