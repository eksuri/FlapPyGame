import pygame
from pipe import Pipe

from random import randint

class Pipes(pygame.sprite.Group):
    
    def __init__(self, width, density, color):
        pygame.sprite.Group.__init__(self)
        self.width = width
        self.density = density
        self.counter = self.width / self.density
        self.color = color
        self.add(Pipe(0,0,color,0))

    def update(self):
        self.counter -= 1
        if self.counter < 0:
            self.add(Pipe(0,0, self.color,0))
            self.counter = self.width / self.density
        pygame.sprite.Group.update(self)