"""
module for drawing things
"""
import pygame
"""
variables globales 
"""
global hight_tile 
global width_tile
hight_tile = 60
width_tile = 70

def draw_line_hex(nb, image, pos, background):
    """
    dessine une ligne d'image
    """
    for i in range(nb+1):
        background.blit(image, pos)
        pos[0] += width_tile 

def draw_bord(nb, imageA, imageB, background):
    """
    affiche le plateau de jeu 
    """
    images = [imageA, imageB]
    pos = [0, 0]
    for i in range(nb+1):
        draw_line_hex(nb, images[i%2], pos, background)
        pos[0] = 0
        pos[1] += hight_tile
