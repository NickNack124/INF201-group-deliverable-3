
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
        time.sleep(1.5)
        self.hero.attack(self.enemy)
        time.sleep(1.5)

        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulate_battle(self):
        """Simulates a full battle between the two characters."""
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()

        time.sleep(1.5)
        if self.hero.is_alive:
            print(f'{self.hero.name} wins!')
        else:
            print(f'{self.enemy.name} wins!')
