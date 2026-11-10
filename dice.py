
"""A module containing the "Dice" class definition."""

import random as rd


class Dice:
    """A dice that adds variability to several parts of a text-based RPG."""


    def __init__(self, sides=6):
        """Initializes the Dice class with a specified number of sides."""
        if sides < 2:
            raise ValueError("Dice must have at least 2 sides.")
        self.sides = sides


    def roll(self):
        """Rolls the dice and returns a random integer between 1 and the number of sides."""
        result = rd.randint(1, self.sides)
        return print(f"The dice rolled a {result}")


    def __repr__(self):
        """Representation of the Dice object."""
        return f'Dice(sides={self.sides})'
    

    def describe(self):
        """Provides a description of the dice."""
        return f"This is a {self.sides}-sided dice."

