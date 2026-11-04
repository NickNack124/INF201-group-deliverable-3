"""
A module containing the updated "Character" class-definition,
as well as any related class-definitions.
"""

import random as rd

from game_simulator_v1 import Character as Char
from items import Weapon


class Character(Char):
    """An updated class-definition of the existing Character-class, with more attributes."""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon | None = None) -> None:
        """
        Initialize the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
            weapon (Weapon | None): Optional weapon that modifies the damage dealt (default = None)
        """
        # Inherured arguments
        super().__init__(
            name=name,
            hp_max=hp_max,
            damage=damage
        )
        # Defining protected versions of the read-only variables
        self._hp = hp_max
        self._is_alive = True
        # Optional weapon attribute
        self.weapon = weapon

    def take_damage(self, damage_received: int) -> None:
        """Receive damage from a damage-source, and subtract HP accordingly."""
        if self._is_alive:
            self._hp = max(0, self._hp - damage_received)
            print(f"{self.name} took {damage_received} damage. Current health: {self._hp} HP.")

            if not self._is_alive:
                # To add some variety, we randomized the death message in case a character dies
                print(
                    rd.choice([
                        f"{self.name} has fallen. May the worms feed on their remains.",
                        f"The one known as {self.name} is no more. May they rest in peace.",
                        f"The brightest lights burn the fastest, and it was {self.name}'s time to fizzle out.",
                        f"Ashes to ashes, dust to dust. May {self.name} find peace in the beyond."
                    ])
                )
        else:
            print(f"{self.name} won't get any deader than dead!")

    def heal(self, healing_received: int) -> None:
        """Restores HP when receiving healing from a healing-source."""
        if self._is_alive:
            self._hp = min(self.hp_max, self._hp + healing_received)
            print(f"{self.name} has been healed for {healing_received} HP. Current health: {self._hp} HP.")
        else:
            print(f"{self.name} must be revived first if they wish to be healed.")

    def attack(self, target: Character) -> None:
        """Attack and deal damage to target character"""
        if target.is_alive:
            if type(self.weapon) is None:
                # The damage dealt with no weapon
                damage_received = self.damage
                print(f"{self.name} swung their fist directly at {target.name}!")

            elif type(self.weapon) is Weapon:
                # Rather than replacing the damage-dealt entirily, we chose to have the weapon modify the damage dealt
                # This way, two characters of differing strength (damage) wielding the same weapon,
                # deal different amounts of damage
                damage_received = round(self.damage + ((self.damage / 10) * self.weapon.roll_damage()))
                print(f"{self.name}, wielding the mighty {self.weapon.name}, launches an attack at {target.name}!")
            target.take_damage(damage_received)
        else:
            print(f"Beating a dead horse, are we? LET {(target.name).upper()} REST!")

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Public read-only property to inspect living-condition without allowing direct, unsafe edits."""
        if self._hp <= 0:
            self._is_alive = False
        return self._is_alive
