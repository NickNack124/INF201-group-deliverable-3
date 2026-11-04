
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

    def roll_damage(self) -> int:
        """Rolls the amount of damage the weapon should deal"""
        return self.damage_dice.roll()

    def __repr__(self) -> str:
        """Representation of weapon object"""
        return f"<Weapon name={self.name} damage_dice={self.damage_dice}>)"

    def __str__(self) -> str:
        """String representation of weapon object"""
        return f"Character: {self.name} with {self.damage_dice} as its damage-dice"
