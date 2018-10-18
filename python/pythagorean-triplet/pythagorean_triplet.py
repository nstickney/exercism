#!/usr/bin/env python3
"""
A Pythagorean triplet is a set of three natural numbers, {a, b, c}, for which,

a**2 + b**2 = c**2

For example,

3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
"""

__author__ = "Stick"
__license__ = "Unlicense"


from sys import argv


def triplets_with_sum(sum_of_triplet):
    """ Calculate the set of Pythagorean triplets found with the given sum """
    result = set()
    for i in range(1, sum_of_triplet // 3 + 1):
        for j in range(i, (sum_of_triplet - i) // 2 + 1):
            if i ** 2 + j ** 2 == (sum_of_triplet - i - j) ** 2:
                result.add((i, j, sum_of_triplet - i - j))
    return result


def main(num):
    """ Run the program """
    print(triplets_with_sum(num))


def print_usage():
    """ Print a helpful usage message """
    print("Usage: python[3]", argv[0], "<natural number>")
    exit(1)


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print_usage()
    main(int(argv[1]))
