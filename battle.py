
"""A module containing the "Battle" class-definition."""

import random as rd
import time

from character import Character, Mage, Warrior


class Battle:
    """A battle-manager class meant to handle the procedures of characters battling eachother."""

    def __init__(self, ch1, ch2):
        """Initializes the Battle class with two characters."""
        self.ch1 = ch1    
        self.ch2 = ch2     

    def play_round(self):
        """Simulates a single round of battle between two characters."""
        self.ch1.attack(self.ch2)

        if self.ch2.is_alive:
            self.ch2.attack(self.ch1)

    def simulate_battle(self):
        """Simulates a full battle between the two characters."""  
        while self.ch1.is_alive and self.ch2.is_alive:
            self.play_round()

        if self.ch1.is_alive:
            print(f'{self.ch1.name} wins!')
        else:
            print(f'{self.ch2.name} wins!')
