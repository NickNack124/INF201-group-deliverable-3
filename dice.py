
"""A module containing the "Dice" class definition."""

import random as rd


class Dice:
    """A dice that adds variability to several parts of a text-based RPG."""

    def __init__(self, sides=6):
        """Initializes the Dice class with a specified number of sides."""
        if sides < 2:
            # We set the minimum number of sides to 2
            sides = 2
        self.sides = sides

    def roll(self) -> int:
        """Rolls the dice and returns a random integer between 1 and the number of sides."""
        result = rd.randint(1, self.sides)
        print(f"The dice rolled a {result}")
        return result

    def __repr__(self) -> str:
        """Representation of the Dice object."""
        return f'<Dice(sides={self.sides})>'

    def __str__(self) -> str:
        """Provides a description of the dice."""
        return f"A dice with sides: {self.sides}"

    def __call__(self):
        """The default action that will occur when trying to use an object of this class as a function"""
        return self.roll()
