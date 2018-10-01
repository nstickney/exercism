#!/usr/bin/env python3
"""
Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan gramma,
"every letter") is a sentence using every letter of the alphabet at least once.
The best known English pangram is:
    The quick brown fox jumps over the lazy dog.
"""

__author__ = "Stick"
__version__ = "0.1.0"
__license__ = "Unlicense"


import sys


def is_pangram(string):
    """ Determines if a string is a pangram """
    for i in range(65, 91, 1):
        if chr(i) not in string and chr(i).lower() not in string:
            return False
    return True


if __name__ == "__main__":
    print(is_pangram(sys.argv[1]))
