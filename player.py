"""
module for player
"""
from map1 import Map, Hexagone
RED = 0
BLUE = 1

class Player:
    """
    player can move, use abilities etc.
    """
    def __init__(self, team, position, m, sprite, no = 1, data=[100, 2]):
        """
        sprite est le sprite associé, 
        data est une listes de l'ensemble des données d'un joueur (vie, stats etc ..)
        """
        self.hitpoint = data[0]
        self.pm = data[1]
        self.position = position
        self.team = team
        self.no = no
        self.sprite = sprite
        self.place(m, position)

    def place(self, m, position):
        """
        place le joueur sur la position sauf si l'hexagone est occupé
        """
        hexagone = m.get(position)
        #assert (hexagone.state), "Hexagone already occupied!" 
        print(hexagone.state)
        if hexagone.state:
            self.position = position
            hexagone.switch()
            hexagone.occupant = self

    def move(self, m, position):
        """
        applique un mouvement au joueur en vérifiant la distance et les pm,
        puis en appliquant .place
        """
        dx = abs(position[1] - self.position[1])
        dy = abs(position[0] - self.position[0])
        dist = dx + dy
        print(dist)
        print(self.pm)
        if dist <= self.pm + 1 and dx <= self.pm and dy <= self.pm:
            self.place(m, position)
            self.pm -= dist

    def hitpoint_variation(self, variation):
        """
        change les hitpoints du joueur
        """
        if variation > 0:
            print(self, "take a heal of", variation, "hp.") 
            self.hitpoint = (self.hitpoint + variation) % 100
        else:
            print(self, "take", variation, "hp damage.")
            self.hitpoint = (self.hitpoint + variation)
            if self.hitpoint <= 0:
                self.hitpoint = 0
                print(self, "is dead.")

    def __str__(self):
        color = "(red)"
        if self.team:
            color = "(blue)"
        return "Player" + str(self.no) + color   
"""
def test():
    map1 = Map(5)
    h = map1.get((1, 1))
    print(h)
    player1 = Player(BLUE, (1, 1), map1)
    print(map1)
    print(h)
    print(h.occupant)
    player1.hitpoint_variation(-50)
    player1.hitpoint_variation(20)
    player1.hitpoint_variation(-80)
    #player2 = Player(RED, (1, 1), map1, 2)
"""


