# INF201-group-deliverable-3
A shared repository for the purpose of completing the third 2-week group assignment in INF201.

# Requirements
The required external modules can be found in the "requirements.txt"-file.
There is no missing required input-data in this repository, as the only file we were given directly is the code found within "game_simulator_v1.py".
We felt this was fine to keep within the repository, since it is just more code, after all.

# Premise
The premise is a the making of a rudamentary tabletop RPG (akin to Dungeons & Dragons) using Classes, divided across several modules.
These classes are meant to be relatively scalable for future additional deatures, though many features are not yet implemented.

# Products
The products of this assignments are the modules "dice.py", "character.py", "itens.py" and "battle.py" (along with the notebook).
*  dice.py simulates the process of rolling a dice
*  character.py contains the class-definition for a general character, with methods for attacking, taking damage, healing, introduction, and more.
   In addition, this module contains class-definitions for two subclasses: the defensive Warrior, and the spellcasting Mage.
*  battle.py contains the class-definition for a battle between two characters.