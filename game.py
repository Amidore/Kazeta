"""
class Game 
"""
import processing 
from sprites import Selection, Text, Spell_selection
from map1 import Map
from spells import Spell
import pygame


class Game:
    def __init__(self, clock, plan,
            display_screen, current_char = None, all_sprites = [], running = True):
        self.running = running
        self.clock = clock
        self.plan = plan
        self.display_screen = display_screen
        self.all_sprites = pygame.sprite.OrderedUpdates(all_sprites)
        self.current_char = current_char
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

    def load_data(self, sprites):
        """
        load sprites 
        """
        self.all_sprites.add(sprites)

    def processing_events(self):
        """
        loop of the events during the current frame
        """
        for event in pygame.event.get():
            if processing.quit(event):
                self.process_quit()
                break
            if processing.push_next_turn(event):
                self.next_turn()
                break
            if processing.select_spell(event):
                self.process_spell_select(event)
                break
            if processing.select(event):
                self.process_select(event)
            if processing.deselect(event):
                self.process_deselect()

    def next_turn(self):
        self.process_deselect()
        announce = Text("Arial", 42, "NEXT TURN!",
                self.plan.map_surface)
        self.all_sprites.add(announce) 
        self.draw()
        self.update()
        pygame.time.wait(1000)
        self.all_sprites.remove(announce)
        self.all_sprites.remove(self.current_char.spell_bar)

        print("Next Turn!")

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
            if type(self.selected[1]) == Spell_selection:
                coordinates = processing.get_hex(pygame.mouse.get_pos())
                self.current_char.cast(self.current_char.spells[self.selected[1].index], self.plan.get(coordinates))
            elif  type(self.selected[1]) == Selection and self.plan.get(self.selected[1].coordinates) == self.current_char.place:
                coordinates = processing.get_hex(pygame.mouse.get_pos())
                self.current_char.move_to(self.plan.get(coordinates))

            else:
                self.process_deselect()
                self.process_select(event)
        else:
            coordinates = processing.get_hex(pygame.mouse.get_pos())
            if 0 <= coordinates[0] < 10 and  0 <= coordinates[1] < 10:
                position = processing.get_pixel_hex(coordinates)
                sel = Selection(position, coordinates)
                print(sel.rect)
                self.all_sprites.add(sel)
                self.selected = [True, sel]
            else:
                self.selected = [False, None]

    def process_spell_select(self, event):
        if self.selected[0]:
            self.process_deselect()
            self.process_spell_select(event)
        else:
            nb_spell = processing.get_nb_spell(pygame.mouse.get_pos())
            if nb_spell is not None:
                spell_sel = Spell_selection(nb_spell)
                self.all_sprites.add(spell_sel)
                print(spell_sel.rect)
                self.selected = [True, spell_sel]

            
    def process_deselect(self):
        """
        deselect an hexagone
        """
        if self.selected[0]:
            self.all_sprites.remove(self.selected[1])
            self.selected[0] = False
            self.selected[1] = None

        
            
        
        
