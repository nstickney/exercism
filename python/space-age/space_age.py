#!/usr/bin/env python3
"""
Given an age in seconds, calculate how old someone would be on each planet
"""

__author__ = "Stick"
__version__ = "0.1.0"
__license__ = "Unlicense"


from sys import argv


class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds

    def calc_years(self):
        return self.seconds / 31557600

    def calc_orbits(self, ratio):
        return round(self.calc_years() / ratio, 2)

    def on_earth(self):
        return self.calc_orbits(1)

    def on_jupiter(self):
        return self.calc_orbits(11.862615)

    def on_mars(self):
        return self.calc_orbits(1.8808158)

    def on_mercury(self):
        return self.calc_orbits(0.2408467)

    def on_neptune(self):
        return self.calc_orbits(164.79132)

    def on_saturn(self):
        return self.calc_orbits(29.447498)

    def on_uranus(self):
        return self.calc_orbits(84.016846)

    def on_venus(self):
        return self.calc_orbits(0.61519726)

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
    print("    seconds: age in seconds")
    exit(1)


if __name__ == "__main__":
    if len(argv) != 2:
        print_usage()

    main(int(argv[1]))
