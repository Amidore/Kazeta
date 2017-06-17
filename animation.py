from sprites import Anim_sprite
from game import *
class Animation():
    def __init__(self, sprites, g):
        self.sprites = []
        self.g = g
        for sprite in sprites:
            self.sprites.append(Anim_sprite(sprite))

    def animate_static(self, coordinates):
        for sprite in self.sprites:
            sprite.rect.move_ip(coordinates[0], coordinates[1])
            print(sprite.rect)
            self.g.load_data([sprite])
            self.g.draw()
            self.g.update()
            self.g.all_sprites.remove(sprite)
            sprite.rect.move_ip(-coordinates[0], -coordinates[1])
            self.g.clock.tick(10)
            


