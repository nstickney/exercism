#!/usr/bin/env python3
"""
Have a conversation with a lackadaisical teenager.
"""

__author__ = "Stick"
__license__ = "Unlicense"


from sys import argv


def hey(phrase):
    phrase = phrase.strip()
    if phrase == "":
        return "Fine. Be that way!"
    if phrase.endswith("?"):
        if phrase.isupper() and not phrase.islower():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    if phrase.isupper() and not phrase.islower():
        return "Whoa, chill out!"
    return "Whatever."


def main(phrase):
    print(hey(phrase))


def print_usage():
    print("Usage: python[3]", argv[0], "<phrase>")
    print("    phrase: something to say to Bob")
    exit(1)


if __name__ == "__main__":
    if len(argv) != 2:
        print_usage()
    main(argv[1])
