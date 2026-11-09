
"""A module containing the "Battle" class-definition."""

import time


class Battle:
    """A battle-manager class meant to handle the procedures of characters battling eachother."""

    def __init__(self, hero, enemy):
        """Initializes the Battle class with a hero and an enemy character."""
        self.hero = hero    
        self.enemy = enemy     

    def play_round(self):
        """Simulates a single round of battle between the hero and the enemy."""
        self.hero.attack(self.enemy)

        if self.enemy.is_alive():
            self.enemy.attack(self.hero)

    def simulate_battle(self):
        """Simulates a full battle between the hero and the enemy."""
        while self.hero.is_alive() and self.enemy.is_alive():
            self.play_round()

        if self.hero.is_alive():
            print(f'Hero wins!')
        else:
            print(f'Enemy wins!')