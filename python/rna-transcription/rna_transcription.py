#!/usr/bin/env python3
"""
Given a DNA strand, return its RNA complement (per RNA transcription).
"""

__author__ = "Stick"
__version__ = "0.1.0"
__license__ = "Unlicense"


from sys import argv


def to_rna(dna_strand):
    """ Calculate the RNA complement (per RNA transcription) of dna_strand """
    return dna_strand.translate(dna_strand.maketrans("GCTA", "CGAU"))


if __name__ == "__main__":
    print(to_rna(argv[1]))
