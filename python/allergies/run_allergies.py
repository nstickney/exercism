#!/usr/bin/env python3
"""
Given a person's allergy score, determine whether or not they're allergic to a
given item, and their full list of allergies.

The list of items (and their value) that were tested are:
    eggs (1)
    peanuts (2)
    shellfish (4)
    strawberries (8)
    tomatoes (16)
    chocolate (32)
    pollen (64)
    cats (128)
"""

__author__ = "Stick"
__license__ = "Unlicense"


from sys import argv
from allergies import Allergies


def main(score, item=None):
    """ Run the allergies program """
    allergies = Allergies(score)
    if item is None:
        print("Detected allergies:")
        for i in allergies.lst:
            print("  +", i)
    elif allergies.is_allergic_to(item):
        print("Allergy to", item, "detected.")
    else:
        print("No allergy to", item, "detected.")


def print_usage():
    """ Print a helpful usage message """
    print("Usage: python[3]", argv[0], "<allergy_score> [item]")
    exit(1)


if __name__ == "__main__":
    if len(argv) > 1 and argv[1].isdigit():
        if len(argv) == 2:
            main(int(argv[1]))
        else:
            main(int(argv[1]), argv[2])
    else:
        print_usage()
