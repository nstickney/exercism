#!/usr/bin/env python3
"""
Score a single throw of dice in Yacht
"""

__author__ = "Stick"
__version__ = "0.1.0"
__license__ = "Unlicense"


from collections import Counter
from sys import argv


# Score categories
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL HOUSE"
FOUR_OF_A_KIND = "FOUR OF A KIND"
LITTLE_STRAIGHT = "LITTLE STRAIGHT"
BIG_STRAIGHT = "BIG STRAIGHT"
CHOICE = "CHOICE"
YACHT = "YACHT"


def score(dice, category):
    """ Calculate the score for a set of dice for a given category in Yacht """
    if category == ONES:
        return dice.count(1)
    if category == TWOS:
        return 2 * dice.count(2)
    if category == THREES:
        return 3 * dice.count(3)
    if category == FOURS:
        return 4 * dice.count(4)
    if category == FIVES:
        return 5 * dice.count(5)
    if category == SIXES:
        return 6 * dice.count(6)
    if category == FULL_HOUSE:
        check = Counter(dice)
        if len(check) == 2 and list(check.most_common()[0])[1] == 3:
            return sum(int(i) for i in dice)
        return 0
    if category == FOUR_OF_A_KIND:
        check = list(Counter(dice).most_common()[0])
        if check[1] >= 4:
            return 4 * check[0]
        return 0
    if category == LITTLE_STRAIGHT:
        dice = sorted(dice)
        for i in range(1, 5):
            if dice[i] != dice[i - 1] + 1:
                return 0
        if dice[0] == 1:
            return 30
        return 0
    if category == BIG_STRAIGHT:
        dice = sorted(dice)
        for i in range(1, 5):
            if dice[i] != dice[i - 1] + 1:
                return 0
        if dice[0] == 2:
            return 30
        return 0
    if category == CHOICE:
        return sum(int(i) for i in dice)
    if category == YACHT:
        num = dice[0]
        for i in dice:
            if i != num:
                return 0
        return 50


if __name__ == "__main__":
    throw = [int(argv[1]), int(argv[2]), int(argv[3]), int(argv[4]),
             int(argv[5])]
    for i in [ONES, TWOS, THREES, FOURS, FIVES, SIXES, FULL_HOUSE,
              FOUR_OF_A_KIND, LITTLE_STRAIGHT, BIG_STRAIGHT, CHOICE, YACHT]:
        print(i + ":", score(throw, i))
