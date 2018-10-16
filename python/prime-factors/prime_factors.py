#!/usr/bin/env python3
"""
Compute the prime factors of a given natural number.
"""

__author__ = "Stick"
__license__ = "Unlicense"


from sys import argv


def prime_factors(natural_number):
    if natural_number < 1:
        raise ValueError("Cannot prime factor negative numbers or zero")
    factors = []
    for i in range(2, natural_number + 1):
        while natural_number % i == 0:
            factors.append(i)
            natural_number //= i
        if i > natural_number:
            break
    return factors


def main(num):
    print(prime_factors(num))


def print_usage():
    print("Usage: python[3]", argv[0], "<number>")
    exit(1)


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print_usage()
    main(int(argv[1]))
