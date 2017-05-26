"""
module for spells
"""
from character import *
from map1 import *

class Spell():
    def __init__(self, name, resource_cost, pattern, distance, effects):
        self.effects = effects
        self.resource_cost = resource_cost
        self.distance = distance
        self. pattern = pattern
        self.name = name

    def prerequisite(self, caster, end):
        start = caster.place
        if start.dist(end) > distance:
            print("out of range!")
            return False
        if resource_cost > caster.resource.points[0]:
            print("Not enough resource!")
            return False
        return True

    def casted(self, caster, end):
        if self.prerequisite(start, end):
            caster.resource.spend(self.resource_cost)
            target = end.get_content()
            if target is not None:
                print("{} cast the spell {} on {}.".format(
                    caster, self, target))
                for effect in self.effects:
                    effect.resolve(caster, target)

    def __str__(self):
        return self.name

class Effect():
    def __init__(self, category):
        self.category = category

    def resolve(self, caster, target):
        raise NotImplementedError

class Damage(Effect):
    def __init__(self, value):
        Effect.__init__(self, "Damage")
        self.value = value

    def resolve(self, caster, target):
        target.take_damage(self.value)

class Heal(Effect):
    def __init__(self, value):
        Effect.__init__(self, "Heal")
        self.value = value

    def resolve(self, caster, target):
        target.take_Heal(self.value)
