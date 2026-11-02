"""
A module containing the updated "Character" class-definition,
as well as any related class-definitions.
"""

import random as rd

from game_simulator_v1 import Character as Char


class Character(Char):
    """An updated class-definition of the existing Character-class, with more attributes."""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10) -> None:
        """
        Initialize the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
        """
        super().__init__(
            name=name,
            hp_max=hp_max,
            damage=damage
        )
        # Defining protected versions of the read-only variables
        self._hp = hp_max
        self._is_alive = True

    def take_damage(self, damage_received: int) -> None:
        """Receive damage from a damage-source, and subtract HP accordingly."""
        if self._is_alive:
            self._hp = max(0, self._hp - damage_received)
            print(f"{self.name} took {damage_received} damage. Current health: {self._hp} HP.")

            if self._hp == 0:
                self._is_alive = False
                # To add some variety, we randomized the death message
                print(
                    rd.choice([
                        f"{self.name} has fallen. May the worms feed on their remains.",
                        f"The one known as {self.name} is no more. May they rest in peace.",
                        f"The brightest lights burn the fastest, and it was {self.name}'s time to fizzle out.",
                        f"Ashes to ashes, dust to dust. May {self.name} find peace in the beyond."
                    ])
                )
        else:
            print(f"Beating a dead horse, are we? Let {self.name} rest!")

    def heal(self, healing_received: int) -> None:
        """Restores HP when receiving healing from a healing-source."""
        if self._is_alive:
            self._hp = min(self.hp_max, self._hp + healing_received)
            print(f"{self.name} has been healed for {healing_received} HP. Current health: {self._hp} HP.")
        else:
            print(f"{self.name} must be revived first if they wish to be healed.")

    def attack(self, target: Character) -> None:
        """Attack and deal damage to target character"""
        print(f"{self.name} launched an attack towards {target.name}!")
        target.take_damage(damage_received=self.damage)

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Public read-only property to inspect living-condition without allowing direct, unsafe edits."""
        return self._is_alive
