"""
class Game 
"""
import processing 
from sprites import Selection
from map1 import Map
import pygame


class Game:
    def __init__(self, clock, plan,
            display_screen, all_sprites = [], running = True):
        self.running = running
        self.clock = clock
        self.plan = plan
        self.display_screen = display_screen
        self.all_sprites = pygame.sprite.Group(all_sprites)
        self.selected = [False, None]

    def run(self):
        """
        loop of the game
        """
        while self.running:
            self.clock.tick(40)
            self.processing_events()
            self.draw()
            self.update()

    def update(self):
        """
        updating the sreen
        """
        pygame.display.update()

    def draw(self):
        """
        erase all with the draw of the board and then draw sprites
        """
        self.plan.draw_map(self.display_screen)
        self.all_sprites.draw(self.display_screen)

    def load_data(self, all_sprites):
        """
        load sprites 
        """
        self.all_sprites = all_sprites

    def processing_events(self):
        """
        loop of the events during the current frame
        """
        for event in pygame.event.get():
            if processing.quit(event):
                self.process_quit()
                break
            if processing.select(event):
                self.process_select(event)
            if processing.deselect(event):
                self.process_deselect()

    def process_quit(self):
        """
        quit the game
        """
        self.running = False

    def process_select(self, event):
        """
        select an hexagone
        """
        if self.selected[0]:
            self.process_deselect()
            self.process_select(event)
        else:
            coordinates = processing.get_hex(pygame.mouse.get_pos())
            position = processing.get_pixel_hex(coordinates)
            sel = Selection(position)
            print(sel.rect)
            self.all_sprites.add(sel)
            self.selected = [True, sel]
            
    def process_deselect(self):
        """
        deselect an hexagone
        """
        if self.selected[0]:
            self.all_sprites.remove(self.selected[1])
            self.selected[0] = False
            self.selected[1] = None

        
            
        
        
