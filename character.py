"""
A module containing the updated "Character" class-definition,
as well as any related class-definitions.
"""

import random as rd
import time

import items
from dice import Dice
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
        super().__init__(
            name=name,
            hp_max=hp_max,
            damage=damage
        )
        # We turn float, str(int | float) and complex.real into integers
        self.damage = abs(int(round(damage.real)))
        # Setting a lower limit on hp (no upper limit yet for scalability)
        self.hp_max = max(abs(int(round(hp_max.real))), 1)
        self._hp = self.hp_max

        # Defining protected version(s) of read-only variable(s)
        self._is_alive = True

        # Attributes from optional items
        self.weapon = weapon
        self.armor = armor

        # "ac" = "armor class" = how much it protects the wearer
        self.ac = self.armor.value() if self.armor else 0
        self.armor_name = self.armor.name if self.armor else "nothing"
        self.weapon_name = self.weapon.name if self.weapon else "nothing"

    def stats(self) -> str:
        """Sends a message about the character's stats"""
        return f"- {self.name}: {self._hp}/{self.hp_max} HP (+{self.ac} AC).\n"

    def take_damage(self, damage_received: int) -> None:
        """Receive damage from a damage-source, and subtract HP accordingly."""
        if not self._is_alive:
            print(f"{self.name} won't get any deader than dead!\n")
            time.sleep(1)
            return

        # The damage received (reduced by worn armor)
        damage_received = max(0, damage_received - self.ac)
        self._hp = max(0, self._hp - damage_received)

        print(f"{self.name} took {damage_received} damage.")
        print(f"{self.stats()}")

        # Checks if character has died from this damage or not
        self.death()

    def heal(self, healing_received: int) -> None:
        """Restores HP when receiving healing from a healing-source."""
        if not self._is_alive:
            print(f"{self.name} must be revived first if they wish to be healed.\n")
            time.sleep(1)
            return

        self._hp = min(self.hp_max, self._hp + healing_received)
        print(f"{self.name} has been healed for {healing_received} HP.")
        print(self.stats())

    def default_attack(self, target: Character) -> int:
        """Does a damage calculation that can be performed by any class"""
        if self.weapon is None:
            # The damage dealt with no weapon
            print(f"{self.name} swung their fist directly at {target.name}!")
            return self.damage

        # Rather than replacing the damage-dealt entirily, we chose to have the weapon modify
        # the damage dealt. This way, two characters of differing strength (damage) wielding
        # the same weapon, deal different amounts of damage.
        damage_received = self.damage + round((self.damage / 10) * self.weapon.roll_damage())
        print(f"{self.name}, wielding the mighty {self.weapon.name}, launches an attack at {target.name}!")
        return damage_received

    def attack(self, target: Character) -> None:
        """Attack and deal damage to target character"""
        if not self.is_alive:
            # We make sure a dead character can't attack
            print(f"{self.name} is dead and can't attack.")
            return

        if not target.is_alive:
            print(f"Beating a dead horse, are we? LET {(target.name).upper()} REST!")
            return

        damage_received = self.default_attack(target)
        target.take_damage(damage_received)

    def death(self) -> None:
        """To add some variety, we randomized the death message for when a character dies"""
        if not self.is_alive:
            time.sleep(1.5)
            print(rd.choice([
                f"{self.name} has fallen. May the worms feed on their remains.\n",
                f"The one known as {self.name} is no more. May they rest in peace.\n",
                f"The brightest lights burn the fastest, and it was {self.name}'s time to fizzle out.\n",
                f"Ashes to ashes, dust to dust. May {self.name} find peace in the beyond.\n"
                ])
            )

    def __repr__(self) -> str:
        """Representation of character object (with the added attributes)"""
        return \
        f"<Character(name={self.name}, hp={self.hp}, damage={self.damage}, "\
        f"weapon={self.weapon_name}, armor={self.ac})>"

    def __str__(self) -> str:
        """String representation of character object (does not need to show equipment)"""
        return \
        f"Character: {self.name} with {self.hp} HP and {self.damage} damage, "\
        f"wielding {self.weapon_name} and wearing {self.armor_name} with value {self.ac}."

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
        self.ac = self.armor.value()
        self.armor_name = self.armor.name

    # Since we chose to give every character the ability to wear armor, we decided to give
    # the warrior a special ability as well, to make them more unique
    def death(self) -> None:
        """The warrior stubbornly tries to cling on to life if their HP reach 0"""
        if self._hp == 0:
            time.sleep(1.5)
            print(f"{self.name} feels a beating in his heart...")

            time.sleep(2)
            if Dice(20).roll() > 15:
                # The warrior rolls more than 15, letting them recover a random amount of health
                time.sleep(1.5)
                print(f"{self.name} is not finished yet!!")
                recovery = Dice(20).roll()
                time.sleep(0.5)
                self.heal(recovery)
            else:
                time.sleep(1.5)
                print("False alarm. It was just rigor mortis.")
                time.sleep(0.5)
                super().death()

    def __repr__(self) -> str:
        """Representation of warrior object"""
        return \
        f"<Warrior(name={self.name}, hp={self.hp}, damage={self.damage}, "\
        f"weapon={self.weapon_name}, armor={self.ac})>"

    def __str__(self) -> str:
        """String representation of warrior object (does not need to show equipment)"""
        return \
        f"Warrior: {self.name} with {self.hp} HP and {self.damage} damage, "\
        f"wielding {self.weapon_name} and wearing {self.armor_name} with value {self.ac}."


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
        # Ensuring mana max is not below 0 (and treating it as valid in as many ways as we can)
        self.mana_max = abs(int(round(mana_max.real, 0)))
        self._mana = self.mana_max

    def stats(self) -> str:
        """Sends a message about the character's stats"""
        return f"- {self.name}: {self.hp}/{self.hp_max} HP (+{self.ac} AC). Mana: {self._mana}/{self.mana_max}\n"

    def attack(self, target: Character) -> None:
        """Attack and deal damage to target character"""
        if not self._is_alive:
            print(f"{self.name} is dead and can't attack.\n")
            time.sleep(1)
            return

        if not target.is_alive:
            print(f"Beating a dead horse, are we? LET {(target.name).upper()} REST!\n")
            time.sleep(1)
            return

        if self._mana >= 10:
            # The damage dealt from a magical attack
            damage_received = self.damage * 2
            self._mana -= 10
            print(f"{self.name} shot an arcane projectile at {target.name}!")
        else:
            # restore 5 mana
            self._mana = min(self.mana_max, self._mana + 5)
            damage_received = self.default_attack(target)

        target.take_damage(damage_received)

    def __repr__(self) -> str:
        """Representation of mage object"""
        return \
        f"<Mage(name={self.name}, hp={self.hp}, mana={self.mana}, damage={self.damage}, "\
        f"weapon={self.weapon_name}, armor={self.ac})>"

    def __str__(self) -> str:
        """String representation of warrior object (does not need to show equipment)"""
        return \
        f"Mage: {self.name} with {self.hp} HP, {self.damage} damage and {self.mana} mana, "\
        f"wielding {self.weapon_name} and wearing {self.armor_name} with value {self.ac}."

    @property
    def mana(self) -> int:
        """'Public read-only property to inspect mana without allowing direct, unsafe edits.'"""
        return self._mana
