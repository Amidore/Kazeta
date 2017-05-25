"""
functions for processing events
"""
import pygame
global hight_tile 
global width_tile
hight_tile = 60
width_tile = 70

def quit(event):
    return event.type == pygame.QUIT


def select(event):
    return event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]

def deselect(event):
    return event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]

def get_hex(pos):
    """
    return the coordinates of the hexagone of the pixel at the position pos
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


def get_pixel_hex(coordinates):
    """
    return the top left edge of the bounding rectangle of the hexagon
    """
    r = width_tile // 2
    x = coordinates[1] * 2 * r
    y = coordinates[0] * hight_tile 
    if not(coordinates[0] % 2):
        x += r
    return (x, y)
    
        

