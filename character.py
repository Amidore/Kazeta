"""
module for characters
"""
from math import ceil
from map1 import *
from processing import get_pixel_hex
import pygame

class Character:
    def __init__(self, name, sprite, spell_bar, place,
            hp, resource, mp, elemental_points, resists,
            spells, states = []):
        self.name = name

        self.sprite = sprite
        self.place = place
        place.add_content(self)
        coordinates = get_pixel_hex(place.coordinates)
        self.sprite.rect.move_ip(coordinates[0], coordinates[1])

        self.spell_bar = spell_bar

        self.hp = [hp, hp]
        self.resource = resource
        self.mp = [mp, mp]
        self.elemental_points = elemental_points
        self.resists = resists

        self.spells = spells
        self.states = states

        place.add_content(self)

    def take_damage(self, value):
        """
        current hp reduce by value 
        (watch out value need to be positiv)
        """
        self.hp[0] -= value
        if self.hp[0] < 0:
            self.hp[0] = 0

        print("{} take {} of damage.".format(self, value))

    def take_heal(self, value):
        """
        current hp increase by value 
        (watch out value need to be positiv)
        """
        self.hp[0] += value
        if self.hp[0] > self.hp[1]:
            self.hp[0] = self.hp[1]

        print("{} receive a heal of {}.".format(self, value))
    
    def receive_state(self, state):
        """
        add a state
        """
        self.states.append(state)

        print("{} is affected by the state {}.".format(self, state.category))
        

    def remove_state(self, state):
        """
        remove the state
        """
        for (i,current_state) in enumerate(self.states):
            if current_state.category == state:
                self.states.pop(i)

        print("{} is not anymore affected by the state {}.".format(
            self, state.category))

    def move_to(self, destination):
        distance = self.place.dist(destination)
        if self.mp[0] < distance:
            print("It is too far!")
        else:
            self.mp[0] -= distance
            destination.add_content(self)
            self.place.clear_content()
            self.place = destination
            coordinatesPixel = get_pixel_hex(destination.coordinates)
            self.sprite.rect = (coordinatesPixel[0], coordinatesPixel[1])

        print("{} moves to {}.".format(self, destination))

    def refill_mp():
        self.mp[0] = self.mp[1]

    def add_mp(self, value):
        self.mp[0] += value
        if self.mp[0] > self.mp[1]:
            self.add_mp()

    def cast(self, spell, target):
        spell.casted(self, target)


    def __str__(self):
        return self.name

class State:
    def __init__(self, category):
        self.category = category

class Resource:
    def __init__(self, category, points):
        self.category = category
        self.points = [points, points]

    def spend(self, value):
        """
        spend the resource 
        watch out points[0] - value need to be positiv and value also
        """
        self.points[0] -= value

    def increase(self, value):
        """
        increase the resource by value
        watch out value need to be positiv
        """
        self.points[0] += value 
        if self.points[0] > self.points[1]:
            self.points[0] = self.points[1]

    def refill(self):
        """
        refill the resource depending on the category
        """
        raise NotImplementedError

class Mana(Resource):
    def __init__(self, value):
        Resource.__init__(self, "Mana", value)

    def refill(self):
        self.increase(ceil(0.1 * self.points[1]))

class Energy(Resource):
    def __init__(self, value):
        Resource.__init__(self, "Energy", value)

    def refill(self):
        self.points[0] = self.points[1]

class Rage(Resource):
    def __init__(self, value):
        Resource.__init__(self, "Rage", value)
        self.points[0] = 0

    def refill(self):
        self.spend(ceil(0.2 * self.points[0]))



        
