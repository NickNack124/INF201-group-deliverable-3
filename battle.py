
"""A module containing the "Battle" class-definition."""

import random as rd
import time

from character import Character


class Battle:
    """A battle-manager class meant to handle the procedures of characters battling eachother."""

    def __init__(self, hero: Character, enemy: Character) -> None:
        """Initializes the Battle class with two characters."""
        self.hero = hero
        self.enemy = enemy

    def play_round(self, round: int = 1) -> None:
        """Simulates a single round of battle between two characters."""
        # We also use a formula to accelerate the time it takes as rounds increase
        time.sleep(2 * 2**(-0.2 * round))
        print(f"ROUND {round}:")
        time.sleep(0.5 * 2**(-0.2 * round))
        self.hero.attack(self.enemy)

        time.sleep(2 * 2**(-0.2 * round))
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulate_battle(self) -> str:
        """Simulates a full battle between the two characters."""
        round = 0
        while self.hero.is_alive and self.enemy.is_alive:
            round += 1
            if round > 30:
                time.sleep(2)
                print("NO MORE! This battle has gone on for long enough!")
                print("I shall declare the victor...")
                break
            else:
                self.play_round(round)

        time.sleep(2)
        if round > 30 and self.hero.is_alive and self.enemy.is_alive:
            winner = rd.choice([self.enemy, self.hero])
            return f'{(winner.name).upper()} WINS!!'
        else:
            if self.hero.is_alive and not self.enemy.is_alive:
                return f'{(self.hero.name).upper()} WINS!!'
            else:
                return f'{(self.enemy.name).upper()} WINS!!'

    def __repr__(self) -> str:
        """How the class should be represented when called on its own"""
        return f'<Battle(hero={self.hero}, enemy={self.enemy})>'

    def __str__(self) -> str:
        """A description of the battle"""
        return f'A might battle between hero: {self.hero} and enemy: {self.enemy}'
