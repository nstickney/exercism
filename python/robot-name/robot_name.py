#!/usr/bin/env python3
"""
Manage robot factory settings.
"""

__author__ = "Stick"
__license__ = "Unlicense"


from random import randint as ri


class Robot:
    """ Factory robots with different names """

    robots = list()

    def __init__(self):
        self.name = self.generate_name()
        self.robots.append(self.name)

    def generate_name(self):
        """ Randomly generate an available name of the form AA000 """
        name = ""
        while name == "" or name in self.robots:
            name = chr(ri(65, 91)) + chr(ri(65, 91)) + str(ri(100, 1000))
        return name

    def reset(self):
        """ Reset a robot to factory defaults (and a new name) """
        old_name = self.name
        self.name = self.generate_name()
        self.robots.remove(old_name)
