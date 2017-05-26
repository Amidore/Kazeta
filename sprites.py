"""
class of sprites
"""
import pygame

class Selection(pygame.sprite.Sprite):
    """
    class of a sprite of selection 
    """
    def __init__(self, pos, coordinates):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./sprites/selection.png').convert()
        self.image.set_colorkey(pygame.Color(34, 177, 76))
        self.rect = self.image.get_rect()
        print(pos)
        self.rect.move_ip(pos[0], pos[1])
        self.coordinates = coordinates

class Spell_selection(pygame.sprite.Sprite):
    def __init__(self, index):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./sprites/spell_selection.png').convert()
        self.image.set_colorkey(pygame.Color(34, 177, 76))
        self.rect = self.image.get_rect()
        self.rect.move_ip(4 + index * 32, 625)
        self.index = index

class Perso(pygame.sprite.Sprite):
    def __init__(self, sprite):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite).convert()
        self.image.set_colorkey(pygame.Color(192, 192, 192))
        self.rect = self.image.get_rect()

class Spell_bar(pygame.sprite.Sprite):
    def __init__(self, sprite, all_spells):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite).convert()
        self.rect = self.image.get_rect()
        self.rect.move_ip(0, 620)
        for (i, spell) in enumerate(all_spells):
            self.image.blit(spell.icon.image, (4 + i * 32, 5)) 
"""
    def selection_spell(self, index):
        sel = pygame.image.load('./sprites/spell_selection.png').convert()
        sel.set_colorkey(pygame.Color(34, 177, 76))
        self.image.blit(sel, (4 + index * 32, 625))

    def deselection_spell(self, index):
        sel = pygame.image.load('./sprites/spell_selection.png').convert()
        sel.set_colorkey(pygame.Color(34, 177, 76))
        self.image.blit(sel, (4 + index * 32, 625))
"""

class icon_spell(pygame.sprite.Sprite):
    def __init__(self, sprite):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite).convert()
        self.rect = self.image.get_rect()

class Text(pygame.sprite.Sprite):
    def __init__(self, name_font, size, text, background):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont(name_font, size)
        self.image = self.font.render(text, 1, (10, 10, 10))
        self.rect = self.image.get_rect(centerx=background.get_width()/2,
                                        centery=background.get_height()/2)

