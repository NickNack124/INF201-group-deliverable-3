"""
A module containing the updated "Character" class-definition,
as well as any related class-definitions.
"""

import random as rd

import items
from game_simulator_v1 import Character as Char


class Character(Char):
    """An updated class-definition of the existing Character-class, with more attributes."""

    def __init__(
            self,
            name: str,
            hp_max: int = 100,
            damage: int = 10,
            weapon: items.Weapon | None = None,
            armor: items.Armor | None = None
        ) -> None:
        """
        Initialize the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100).
            damage (int): Damage delt when character attacks (default = 10).
            weapon (items.Weapon | None): Optional weapon that modifies the damage dealt (default = None).
            armor (items.Armor | None): Optional armor that modifies the damage received (default = None).
        """
        # Inherited arguments
        super().__init__(name=name, hp_max=hp_max, damage=damage)

        # Defining protected version(s) of read-only variable(s)
        self._is_alive = True

        # Attributes from optional items
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage_received: int) -> None:
        """Receive damage from a damage-source, and subtract HP accordingly."""
        if self._is_alive:
            if type(self.armor) is items.Armor:
                # The damage received, reduced by the worn armor
                damage_received = max(0, damage_received - self.armor.value())

            self._hp = max(0, self._hp - damage_received)
            print(f"{self.name} took {damage_received} damage. Current health: {self._hp} HP.")
            self.death()
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
        if not self._is_alive:
            # We make sure a dead character can't attack
            print(f"{self.name} is dead and can't attack.")

        else:
            if target.is_alive:
                if self.weapon is None:
                    # The damage dealt with no weapon
                    damage_dealt = self.damage
                    print(f"{self.name} swung their fist directly at {target.name}!")

                elif type(self.weapon) is items.Weapon:
                    # Rather than replacing the damage-dealt entirily, we chose to have the weapon modify
                    # the damage dealt. This way, two characters of differing strength (damage) wielding 
                    # the same weapon, deal different amounts of damage.
                    damage_dealt = round(self.damage + ((self.damage / 10) * self.weapon.roll_damage()))
                    print(f"{self.name}, wielding the mighty {self.weapon.name}, launches an attack at {target.name}!")

                target.take_damage(damage_received=damage_dealt)
            else:
                print(f"Beating a dead horse, are we? LET {(target.name).upper()} REST!")

    def death(self) -> None:
        """To add some variety, we randomized the death message for when a character dies"""
        if not self.is_alive:
            print(
                rd.choice([
                    f"{self.name} has fallen. May the worms feed on their remains.",
                    f"The one known as {self.name} is no more. May they rest in peace.",
                    f"The brightest lights burn the fastest, and it was {self.name}'s time to fizzle out.",
                    f"Ashes to ashes, dust to dust. May {self.name} find peace in the beyond."
                ])
            )

    @property
    def is_alive(self) -> bool:
        """
        Public read-only property to inspect living-condition without allowing direct, unsafe edits.
        Also updates the living condition for said character if it finds that the hp is 0.
        """
        if self._hp <= 0:
            self._is_alive = False
        return self._is_alive


class Warrior(Character):
    """A subclass focused on high defense and dealing raw physical damage."""
    def __init__(
            self,
            name: str,
            hp_max: int = 110,                      # Slightly higher default health
            damage: int = 12,                       # Slightly higher default damage
            weapon: items.Weapon | None = None,
            armor: items.Armor | None = None
        ) -> None:
        """
        Initialize the character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100).
            damage (int): Damage delt when character attacks (default = 10).
            weapon (items.Weapon | None): Optional weapon that modifies the damage dealt (default = None).
            armor (items.Armor | None): Armor that modifies the damage received (default = None).
        """
        # Inherited arguments
        super().__init__(
            name=name,
            hp_max=hp_max,
            damage=damage,
            weapon=weapon,
            armor=armor
        )

        # Gives a default armor for the warrior class with a value of 5
        if self.armor is None:
            self.armor = items.Armor(armor=5)


class Mage(Character):
    """A subclass focused on high magical damage, at the cost of mana and lower health."""
    def __init__(
            self,
            name: str,
            hp_max: int = 90,                       # Slightly lower default health
            mana_max: int = 30,
            damage: int = 10,
            weapon: items.Weapon | None = None,
            armor: items.Armor | None = None
        ) -> None:
        """
        Initialize the character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100).
            mana_max (int): The resource used for casting spells (default = 30).
            damage (int): Damage delt when character attacks (default = 10).
            weapon (items.Weapon | None): Optional weapon that modifies the damage dealt (default = None).
            armor (items.Armor | None): Armor that modifies the damage received (default = None).
        """
        # Inherited arguments
        super().__init__(
            name=name,
            hp_max=hp_max,
            damage=damage,
            weapon=weapon,
            armor=armor
        )
        # Defining protected version(s) of read-only variable(s)
        self._mana = mana_max

    def attack(self, target: Character) -> None:
        """Attack and deal damage to target character"""
        if target.is_alive:
            if self._mana >= 10:
                # The damage dealt from a magical attack
                damage_received = self.damage * 2
                print(f"{self.name} shot an arcane projectiile at {target.name}!")
            else:
                # restore 5 mana
                self._mana += 5

                if self.weapon is None:
                    # The damage dealt with no weapon
                    damage_received = self.damage
                    print(f"{self.name} swung their fist directly at {target.name}!")

                elif type(self.weapon) is items.Weapon:
                    # Damage dealt with a weapon
                    damage_received = round(self.damage + ((self.damage / 10) * self.weapon.roll_damage()))
                    print(f"{self.name}, wielding the mighty {self.weapon.name}, launches an attack at {target.name}!")

            target.take_damage(damage_received)
        else:
            print(f"Beating a dead horse, are we? LET {(target.name).upper()} REST!")

    @property
    def mana(self) -> int:
        """'Public read-only property to inspect mana without allowing direct, unsafe edits.'"""
        return self._mana
