
"""A module containing the "Dice" class definition."""

import random as rd


class Dice:
    """A dice that adds variability to several parts of a text-based RPG."""

    def __init__(self, sides=6):
        if sides < 2:
            raise ValueError("Dice must have at least 2 sides.")
        self.sides = sides

        def roll(self):
            return rd.randint(1, self.sides)

        def __repr__(self):
            return f'Dice(sides={self.sides})'

        def __call__(self):
            return self.roll()


d6 = Dice()
d20 = Dice(sides=20)

print(d6)
print(d20.roll())