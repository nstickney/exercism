#!/usr/bin/env python3
"""
Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan gramma,
"every letter") is a sentence using every letter of the alphabet at least once.
The best known English pangram is:
    The quick brown fox jumps over the lazy dog.
"""

__author__ = "Stick"
__license__ = "Unlicense"


import sys
from string import ascii_lowercase


def is_pangram(string):
    """ Determines if a string is a pangram """
    return all(letter in string.lower() for letter in ascii_lowercase)


if __name__ == "__main__":
    print(is_pangram(sys.argv[1]))
