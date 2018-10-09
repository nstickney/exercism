#!/usr/bin/env python3
"""
Score a single throw of dice in Yacht
"""

__author__ = "Stick"
__license__ = "Unlicense"


from sys import argv


# Score dice based on face value:
def sum_value(dice, value):
    return dice.count(value) * value


# Score categories
def ONES(dice):
    return sum_value(dice, 1)


def TWOS(dice):
    return sum_value(dice, 2)


def THREES(dice):
    return sum_value(dice, 3)


def FOURS(dice):
    return sum_value(dice, 4)


def FIVES(dice):
    return sum_value(dice, 5)


def SIXES(dice):
    return sum_value(dice, 6)


def FULL_HOUSE(dice):
    if len(set(dice)) == 2 and 2 <= dice.count(dice[0]) <= 3:
        return sum(dice)
    return 0


def FOUR_OF_A_KIND(dice):
    return 4 * sorted(dice)[2] if dice.count(sorted(dice)[2]) >= 4 else 0


def LITTLE_STRAIGHT(dice):
    return 30 if sorted(dice) == list(range(1, 6)) else 0


def BIG_STRAIGHT(dice):
    return 30 if sorted(dice) == list(range(2, 7)) else 0


def CHOICE(dice):
    return sum(dice)


def YACHT(dice):
    return 50 if all(i == dice[0] for i in dice) else 0


def score(dice, category):
    """ Calculate the score for a set of dice for a given category in Yacht """
    return category(dice)


if __name__ == "__main__":
    throw = [int(argv[1]), int(argv[2]), int(argv[3]), int(argv[4]),
             int(argv[5])]
    for i in [ONES, TWOS, THREES, FOURS, FIVES, SIXES, FULL_HOUSE,
              FOUR_OF_A_KIND, LITTLE_STRAIGHT, BIG_STRAIGHT, CHOICE, YACHT]:
        print(i.__name__ + ":" + " " * (15 - len(i.__name__)), score(throw, i))
