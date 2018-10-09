#!/usr/bin/env python3
"""
Given an age in seconds, calculate how old someone would be on each planet
"""

__author__ = "Stick"
__license__ = "Unlicense"


from sys import argv


class SpaceAge(object):

    RATIOS = [(planet, ratio * 31557600) for planet, ratio in (
        ('mercury',   0.2408467),
        ('venus',     0.61519726),
        ('earth',     1.0),
        ('mars',      1.8808158),
        ('jupiter',  11.862615),
        ('saturn',   29.447498),
        ('uranus',   84.016846),
        ('neptune', 164.79132)
    )]

    def __init__(self, seconds):
        self.seconds = seconds
        for planet, ratio in self.RATIOS:
            setattr(self, 'on_' + planet, self._orbits(ratio, seconds))

    def _orbits(self, ratio, seconds):
        return lambda ratio = ratio: round(seconds / ratio, 2)

    def max_digits(self):
        return len(str(int(self.on_mercury())))


def main(seconds):
    space_age = SpaceAge(seconds)
    digits = space_age.max_digits()
    width = digits + digits // 3 + 3
    print(f'Mercury Years: {space_age.on_mercury(): >#{width},.2f}')
    print(f'Venus Years:   {space_age.on_venus(): >#{width},.2f}')
    print(f'Earth Years:   {space_age.on_earth(): >#{width},.2f}')
    print(f'Mars Years:    {space_age.on_mars(): >#{width},.2f}')
    print(f'Jupiter Years: {space_age.on_jupiter(): >#{width},.2f}')
    print(f'Saturn Years:  {space_age.on_saturn(): >#{width},.2f}')
    print(f'Uranus Years:  {space_age.on_uranus(): >#{width},.2f}')
    print(f'Neptune Years: {space_age.on_neptune(): >#{width},.2f}')


def print_usage():
    print("Usage: python[3]", argv[0], "<seconds>")
    print("    seconds: age in seconds (integer)")
    exit(1)


if __name__ == "__main__":
    if len(argv) != 2:
        print_usage()

    main(int(argv[1]))
