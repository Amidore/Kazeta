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
knight2 = sprites.Perso('./sprites/new_mage.png')
icon_strike = sprites.icon_spell('./sprites/icon_sword_strike.png')

hit = spells.Damage(15)
cac = spells.Spell("strike of sword", icon_strike, 50, 1, 1, [hit])

spell_bar = sprites.Spell_bar('./sprites/ability_bar.png', [cac])

Hero1 = character.Character("Link", knight, spell_bar, game.plan.get((1, 1)),
        100, character.Energy(100), 3,
        None, None, [cac])

Hero2 = character.Character("Zelda", knight2, spell_bar, game.plan.get((1, 2)),
        100, character.Energy(100), 3,
        None, None, [cac])

game.current_char = Hero1
print(type(game.all_sprites))
game.load_data([knight, knight2, spell_bar])

game.run()

pygame.quit()
