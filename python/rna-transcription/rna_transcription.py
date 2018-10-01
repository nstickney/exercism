#!/usr/bin/env python3
"""
Given a DNA strand, return its RNA complement (per RNA transcription).
"""

__author__ = "Stick"
__version__ = "0.1.0"
__license__ = "Unlicense"


import sys


def to_rna(dna_strand):
    """ Calculate the RNA complement (per RNA transcription) of dna_strand """
    dna_strand = dna_strand.replace("A", "U").replace("T", "A")
    return dna_strand.replace("G", "X").replace("C", "G").replace("X", "C")


if __name__ == "__main__":
    print(to_rna(sys.argv[1]))
