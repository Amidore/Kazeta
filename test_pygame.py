"""
affichage et interface test de pygame
"""
import pygame
from player import *
from pygame.locals import *

"""
variables globales 
"""
global hight_tile 
global width_tile

"""
TODO:   - module pour fonction de dessin
        - fonction dans la boucle d'events
"""

def draw_line_hex(nb, image, pos):
    """
    dessine une ligne d'image
    """
    for i in range(nb+1):
        screen.blit(image, pos)
        pos[0] += width_tile 

def draw_select_hexB(coordinates, hexB_top, hexB_bottom):
    """
    dessine un hexagone selectionne de type B
    """
    screen.blit(hexB_top, (
        coordinates[1] * width_tile, coordinates[0] * hight_tile)) 
    screen.blit(hexB_bottom, (
        coordinates[1] * width_tile, (coordinates[0] +1) * hight_tile)) 

def draw_select_hexA(coordinates,
        hexA_top_left,
        hexA_top_right,
        hexA_bottom_left,
        hexA_bottom_right):
    """
    dessine un hexagone selectionne de type A
    """
    screen.blit(hexA_top_left, (
        coordinates[1] * width_tile, coordinates[0] * hight_tile)) 
    screen.blit(hexA_top_right, (
        (coordinates[1] + 1) * width_tile, coordinates[0] * hight_tile)) 
    screen.blit(hexA_bottom_left, (
        coordinates[1] * width_tile, (coordinates[0] +1) * hight_tile)) 
    screen.blit(hexA_bottom_right, (
        (coordinates[1] + 1) * width_tile, (coordinates[0] +1) * hight_tile)) 


def draw_bord(nb, imageA, imageB):
    """
    affiche le plateau de jeu 
    """
    images = [imageA, imageB]
    pos = [0, 0]
    for i in range(nb+1):
        draw_line_hex(nb, images[i%2], pos)
        pos[0] = 0
        pos[1] += hight_tile

"""
def draw_flag(coordinates, flags, color = 0):
    screen.blit(flags[color], (
        (coordinates[1] + 1) * width_tile - 14 - (width_tile / 2) * (
            coordinates[0] % 2),
        20 + hight_tile * coordinates[0]))
"""

def draw_perso(image, coordinates):
    """
    les sprite sont de 50x40 pixel
    """
    screen.blit(image, (
        (coordinates[1] + 1) * width_tile - 25  - (width_tile / 2) * (
            coordinates[0] % 2),
        10 + hight_tile * coordinates[0]))

def draw_effect(effect, coordinates):    
    """
    les sprite sont de 50x40 pixel
    """
    screen.blit(effect, (
        (coordinates[1] + 1) * width_tile - 25  - (width_tile / 2) * (
            coordinates[0] % 2),
        10 + hight_tile * coordinates[0]))

def draw_bar(button, jauges, abilities_bar, fireball_icon):
    """
    dessine la barre de sort 
    """
    for i in range(8):
        screen.blit(abilities_bar, (i * width_tile, 10 * hight_tile))
    screen.blit(jauges, (6 * width_tile, 10 * hight_tile))
    screen.blit(button, (8 * width_tile, 10 * hight_tile))
    screen.blit(fireball_icon, ( 5, 10 * hight_tile + 24))

def get_hex(pos):
    """
    récupère les coordonnées de l'hexagone selon le pixel ciblé
    """
    print(pos)
    m = (2 * width_tile) / (3 * hight_tile)
    parity_line = (pos[1] // hight_tile) % 2
    # parity_raw = (pos[0] - ((1- parity_line) * width_tile / 2)) % width_tile 
    coordinates_section = [pos[1] // hight_tile, pos[0] // width_tile]
    coordinates = [coordinates_section[0], coordinates_section[1]]
    print(coordinates_section)
    if not(parity_line):
        print("pair")
        print(pos[0] - ((coordinates_section[1] * width_tile) + (hight_tile / 2)))
        if pos[0] - (
                (coordinates_section[1] * width_tile) + (
                    hight_tile / 2)) < 0:
            coordinates[1] -= 1 
            if pos[1] - (coordinates_section[0] * hight_tile) < (pos[0] - coordinates_section[1] * width_tile)  * m:
                coordinates[0] -= 1
                coordinates[1] += 1 
        else:
            if pos[1] - (coordinates_section[0] * hight_tile) < ( 2 * hight_tile / 3 - (pos[0] - coordinates_section[1] * width_tile) * m):
                coordinates[0] -= 1
    else:
        print("impair")
        if pos[1] - (
                coordinates_section[0] * hight_tile) < (hight_tile / 3 - (pos[0] - coordinates_section[1] * width_tile) * m):
                coordinates[0] -= 1
                coordinates[1] -= 1
        if pos[1] - (
                coordinates_section[0] * hight_tile) < (- hight_tile / 3 + (pos[0] - coordinates_section[1] * width_tile) * m):
                coordinates[0] -= 1

    return coordinates

    
"""
initialise pygame et charge les sprites de bases pour tracer le plateau
"""
hight_tile = 60
width_tile = 70
pygame.init()
green = pygame.Color(34, 177, 76)
grey = pygame.Color(192, 192, 192)
screen = pygame.display.set_mode((700, 660),pygame.RESIZABLE)
background = pygame.image.load('./sprites/map_resize.png').convert()
hexA = pygame.image.load('./sprites/hexA.png').convert()
hexA.set_colorkey(green)
hexB = pygame.image.load('./sprites/hexB.png').convert()
hexB.set_colorkey(green)

"""
charge les sprites pour la barre de sort
"""
button_next = pygame.image.load('./sprites/next_turn_button.png').convert()
button_next.set_colorkey(green)
jauges = pygame.image.load('./sprites/jauge.png').convert()
jauges.set_colorkey(green)
abilities_bar = pygame.image.load('./sprites/ability_bar.png').convert()
abilities_bar.set_colorkey(green)

fireball_icon = pygame.image.load('./sprites/fireball_icon.png').convert()

"""
charge les sprites pour la selection
"""
selectB_top = pygame.image.load('./sprites/select_hex_top.png').convert()
selectB_top.set_colorkey(green)
selectB_bottom = pygame.image.load('./sprites/select_hex_bottom.png').convert()
selectB_bottom.set_colorkey(green)
selectA_top_left = pygame.image.load('./sprites/select_hexA_top_left.png').convert()
selectA_top_left.set_colorkey(green)
selectA_bottom_left = pygame.image.load('./sprites/select_hexA_bottom_left.png').convert()
selectA_bottom_left.set_colorkey(green)
selectA_top_right = pygame.image.load('./sprites/select_hexA_top_right.png').convert()
selectA_top_right.set_colorkey(green)
selectA_bottom_right = pygame.image.load('./sprites/select_hexA_bottom_right.png').convert()
selectA_bottom_right.set_colorkey(green)

"""
charge les sprites pour les persos et les effets
"""
knight = pygame.image.load('./sprites/knight.png').convert()
knight.set_colorkey(grey)
knight_select = pygame.image.load('./sprites/knight_select.png').convert()
knight_select.set_colorkey(grey)
mage = pygame.image.load('./sprites/mage.png').convert()
mage.set_colorkey(grey)
effect = pygame.image.load('./sprites/effect.png').convert()
effect.set_colorkey(grey)
effect2 = pygame.image.load('./sprites/effect2.png').convert()
effect2.set_colorkey(grey)
target = pygame.image.load('./sprites/target.png').convert()
target.set_colorkey(grey)

"""
trace le plateau
"""
screen.blit(background, (0, 0))
draw_bord(10, hexA, hexB)
draw_bar(button_next, jauges, abilities_bar, fireball_icon)
"""
draw_perso(knight, (1, 1))
draw_perso(knight_select, (1, 5))
draw_perso(mage, (3, 3))
draw_perso(knight, (8, 8))
draw_effect(target, (6, 6))
draw_effect(effect, (1, 1))
draw_effect(effect2, (3, 3))
draw_effect(effect2, (8, 8))
draw_select_hexB((1, 6), selectB_top, selectB_bottom)
draw_select_hexA((2, 3), 
        selectA_top_left,
        selectA_top_right,
        selectA_bottom_left,
        selectA_bottom_right) 
"""

"""
initialisation de variable
"""
clock = pygame.time.Clock()
selected = [False, None]
map1 = Map(10)
player1 = Player(BLUE, (1, 1), map1,knight)
draw_perso(player1.sprite, player1.position)
RUN = 1
while RUN:
    """
    boucle de jeu
    """
    for event in pygame.event.get():
        """
        boucle d'events
        """
        if event.type == QUIT:
            """
            quitter
            """
            RUN = False
        if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            """
            selectionner
            """
            coordinates = get_hex(pygame.mouse.get_pos())
            if coordinates[0] < 0 or coordinates[1] < 0 or coordinates[0] > 9 or coordinates[1] > 9:
                break
            if selected[0]:
                if selected[1][0] % 2:
                    draw_select_hexB(selected[1], hexB, hexA)
                else:
                    draw_select_hexA(selected[1],
                            hexA,
                            hexA,
                            hexB,
                            hexB)
                if selected[1][0] == player1.position[0] and selected[1][1] == player1.position[1]:
                    """
                    deplace le perso selectionné
                    """
                    print("move")
                    player1.move(map1, coordinates)
                    screen.blit(background, (0, 0))
                    draw_bord(10, hexA, hexB)
                    draw_bar(button_next, jauges, abilities_bar, fireball_icon)
                    draw_perso(player1.sprite, player1.position)
            if coordinates[0] % 2:
                draw_select_hexB(coordinates, selectB_top, selectB_bottom)
            else:
                draw_select_hexA(coordinates,
                        selectA_top_left,
                        selectA_top_right,
                        selectA_bottom_left,
                        selectA_bottom_right)
            selected[0] = True
            selected[1] = coordinates
            draw_bar(button_next, jauges, abilities_bar, fireball_icon)

        if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]:
            """
            deselection
            """
            if selected[0]:
                if selected[1][0] % 2:
                    draw_select_hexB(selected[1], hexB, hexA)
                else:
                    draw_select_hexA(selected[1],
                            hexA,
                            hexA,
                            hexB,
                            hexB)
            selected[0] = False
            selected[1] = None

    pygame.display.update()
    clock.tick(40)

pygame.quit()
