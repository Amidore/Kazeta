"""
class of sprites
"""
import pygame

class Selection(pygame.sprite.Sprite):
    """
    class of a sprite of selection 
    """
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./sprites/selection.png').convert()
        self.image.set_colorkey(pygame.Color(34, 177, 76))
        self.rect = self.image.get_rect()
        print(pos)
        self.rect.move_ip(pos[0], pos[1])

class Perso(pygame.sprite.Sprite):
    def __init__(self, sprite):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite).convert()
        self.image.set_colorkey(pygame.Color(192, 192, 192))
        self.rect = self.image.get_rect()
