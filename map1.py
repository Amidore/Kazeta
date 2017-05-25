"""
module map du jeu 
"""
import pygame
import drawing
FREE = 1
BlOCKED = 0
green = pygame.Color(34, 177, 76)

class Hexagone:
    """
    classe des cases hexagonales
    """
    def __init__(self, coordinates = (0, 0), state = FREE):
        """
        state correspond a l'etat libre ou occupe de la case hexagonale
        """
        self.state = state
        self.coordinates = coordinates
    
    def switch(self):
        """
        switch the state of the hex
        """
        self.state = not self.state

    def __str__(self):
        s = "B"
        if self.state:
            s = "F"
        return "Hex({},".format(self.coordinates) + s + ")"


class Map:
    """
    classe pour la map hexagonale 
    """
    def __init__(self, fond, size=30):
        """
        size est la taille, la map est aussi large que longue
        area est un tableau a double entrees remplie d'hexagones 
        """
        self.size = size
        self.area = []
        for i in range(size):
            self.area.append([])
            for j in range(size):
                self.area[i].append(Hexagone((i, j)))

        background = pygame.image.load(fond).convert()
        hexA = pygame.image.load('./sprites/hexA.png').convert()
        hexA.set_colorkey(green)
        hexB = pygame.image.load('./sprites/hexB.png').convert()
        hexB.set_colorkey(green)
        drawing.draw_bord(10, hexA, hexB, background)
        self.map_surface = background

    def get(self, coordinates):
        """
        return the hex of the map at the (x, y) coordinates
        """
        return self.area[coordinates[0]][coordinates[1]]

    def draw_map(self, display_screen):
        """
        draw the map surface
        """
        display_screen.blit(self.map_surface, (0, 0))

    def __str__(self):
        s = ""
        for i in range(self.size):
            if i % 2:
                s += "    "
            for j in range(self.size):
                s += str(self.area[i][j]) + " "
            s += "\n"
        return s

def test():
    map1 = Map(5)
    print(map1)
    h1 = map1.get((0,0))
    print(h1)
    h1.switch()
    print(h1)
    print(map1)
