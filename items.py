
"""A module containing the class-definitions for specific item-types."""

from dice import Dice


class Weapon:
    """Items meant to be wielded by characters to effect damage-dealing calculations."""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        """
        Initialize the Weapon

        Args:
            name (str): The name of the weapon.
            damage_dice (Dice): The damage-calculating dice-configuration.
        """
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self, damage_dice: Dice) -> int:
        """Rolls the amount of damage the weapon should deal"""
        return self.damage_dice.roll()
