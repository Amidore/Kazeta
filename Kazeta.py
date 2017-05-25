"""
executable
"""
import pygame
from game import Game
from map1 import Map

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((700, 660),pygame.RESIZABLE)
plan = Map('./sprites/map_resize.png')

game = Game(clock, plan, screen)

game.run()

pygame.quit()
