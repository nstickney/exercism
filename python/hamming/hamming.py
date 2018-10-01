#!/usr/bin/env python3
"""
Calculate the Hamming difference between two DNA strands
"""

__author__ = "Stick"
__version__ = "0.1.0"
__license__ = "Unlicense"


import sys


def distance(seq1, seq2):
    """ Calculate the Hamming difference between two DNA strands """
    if len(seq1) != len(seq2):
        raise ValueError("Unequal sequence lengths:", seq1, seq2)
    return sum(1 for i, j in zip(seq1, seq2) if i != j)


if __name__ == "__main__":
    print(distance(sys.argv[1], sys.argv[2]))
