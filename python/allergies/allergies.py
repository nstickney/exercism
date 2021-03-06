#!/usr/bin/env python
""" Determine allergies based on allergy score """


class Allergies:
    """ Determine allergies based on allergy score """

    allergens = [
        "eggs",
        "peanuts",
        "shellfish",
        "strawberries",
        "tomatoes",
        "chocolate",
        "pollen",
        "cats"
    ]

    def __init__(self, score):
        self.score = score

    def is_allergic_by_index(self, index):
        """ Determine if score represents allergy to an item given by index """
        return bool(self.score >> index & 1)

    def is_allergic_to(self, item):
        """ Determine if the score represents an allergy to a specific item """
        return self.is_allergic_by_index(self.allergens.index(item))

    @property
    def lst(self):
        """ Determine the list of allergens the allergy score represents """
        return [self.allergens[i] for i in range(len(self.allergens))
                if self.is_allergic_by_index(i)]
