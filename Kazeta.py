"""
executable
"""
import pygame
from game import Game
from map1 import Map
import character
import spells
import sprites

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((700, 660),pygame.RESIZABLE)
plan = Map('./sprites/map_resize.png')

game = Game(clock, plan, screen)


knight = sprites.Perso('./sprites/new_knight.png')

hit = spells.Damage(15)
cac = spells.Spell("strike of sword", 50, 1, 1, hit)
Hero1 = character.Character("Link", knight, game.plan.get((1, 1)),
        100, character.Energy(100), 3,
        None, None, [cac])
print(type(game.all_sprites))
game.load_data(knight)

game.run()

pygame.quit()
