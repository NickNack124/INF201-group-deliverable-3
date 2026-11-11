
"""A module containing the "Battle" class-definition."""

import random as rd
import time

from character import Character


class Battle:
    """A battle-manager class meant to handle the procedures of characters battling eachother."""

    def __init__(self, hero: Character, enemy: Character):
        """Initializes the Battle class with two characters."""
        self.hero = hero
        self.enemy = enemy

    def play_round(self):
        """Simulates a single round of battle between two characters."""
        time.sleep(2)
        self.hero.attack(self.enemy)

        time.sleep(2)
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulate_battle(self):
        """Simulates a full battle between the two characters."""
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()

        time.sleep(1)
        if self.hero.is_alive:
            print(f'{self.hero.name} wins!')
        else:
            print(f'{self.enemy.name} wins!')

    def __repr__(self) -> str:
        """How the class should be represented when called on its own"""
        return f'<Battle(hero={self.hero}, enemy={self.enemy})>'

    def __str__(self):
        """A description of the battle"""
        return f'A might battle between hero: {self.hero} and enemy: {self.enemy}'
