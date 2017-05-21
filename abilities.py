"""
module of generic abilities
"""

from player import Player
BURST = 0
HEAL = 1
EFFECT = [ -1, 1]

class Ability:
    """
    an instance of a cast of an ability
    """
    def __init__(self, category, target, data):
        self.category = category
        self.target = target
        self.data = data

    def process(self):
        if self.category:
            print(self.target, "is targeted by a healing touch.")
        else:
            print(self.target, "is targed by a fireball.")
        self.target.hitpoint_variation(
                EFFECT[self.category] * self.data[0])

def cast_fireball(caster, target):
    """
    lance une fireball
    """
    spell = Ability(BURST, target, [20])
    print(caster, "casts a fireball.")
    spell.process()


