"""
executable
"""
import pygame
from game import Game
from map1 import Map
import character
import spells
import sprites
import animation
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 660),pygame.RESIZABLE)
plan = Map('./sprites/map_resize.png')

game = Game(clock, plan, screen)


knight = sprites.Perso('./sprites/new_knight.png')
link_icon = sprites.icon_spell('./sprites/link_icon.png')
mage = sprites.Perso('./sprites/new_mage.png')
mage_icon = sprites.icon_spell('./sprites/mage_icon.png')


dot_anim = animation.Animation(['./sprites/dot_1.png',
                    './sprites/dot_2.png',
                    './sprites/dot_3.png',
                    './sprites/dot_4.png',
                    './sprites/dot_5.png',
                    './sprites/dot_6.png'], game)

hot_anim = animation.Animation(['./sprites/hot_1.png',
                    './sprites/hot_2.png',
                    './sprites/hot_3.png',
                    './sprites/hot_4.png',
                    './sprites/hot_5.png',
                    './sprites/hot_6.png'], game)


icon_strike = sprites.icon_spell('./sprites/icon_sword_strike.png')
icon_fireball = sprites.icon_spell('./sprites/icon_fireball.png')
icon_touch_of_heal = sprites.icon_spell('./sprites/icon_touch_of_heal.png')

splash = spells.Damage(25)
slight_heal = spells.Heal(30)
hit = spells.Damage(15)
cac = spells.Spell("strike of sword", icon_strike, 50, 1, 1, [hit])
fireball = spells.Spell("Fireball", icon_fireball, 75, 1, 5, [splash])
toh = spells.Spell("Touch of heal", icon_touch_of_heal, 55, 1, 3, [slight_heal])

spell_5_WW = spells.Spell("Production", icon_fireball, 20, dot_anim, 4,
        [spells.Dot(3, 20)]) 
spell_5_H = spells.Spell("Production", icon_touch_of_heal, 20, hot_anim, 4,
        [spells.Hot(3, 20)])


spell_bar1 = sprites.Spell_bar('./sprites/ability_bar.png', [cac, spell_5_WW, spell_5_H])
spell_bar2 = sprites.Spell_bar('./sprites/ability_bar.png', [fireball, toh])

Hero1 = character.Character("Link", knight, link_icon, spell_bar1, game.plan.get((1, 1)),
        100, character.Energy(100), 3,
        None, None, [cac,spell_5_WW, spell_5_H], [])

Hero2 = character.Character("Zelda", mage, mage_icon, spell_bar2, game.plan.get((1, 5)),
        80, character.Mana(150), 3,
        None, None, [fireball, toh], [])


game.load_chars([Hero1, Hero2])
game.load_data(sprites.Side_bar(game.list_char))
game.load_data(sprites.Current_selection(0))

game.run()

pygame.quit()
