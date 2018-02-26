import pygame
from globals import *
from ground import Ground

class Grounds(pygame.sprite.Group):
    
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        self.range = range(0, WIDTH + 336, 336)
        for x in self.range:
            self.add(Ground(336, x, len(self.range)))

    def update(self):
        pygame.sprite.Group.update(self)

    def die(self):
        for ground in pygame.sprite.Group.sprites(self):
            ground.die()