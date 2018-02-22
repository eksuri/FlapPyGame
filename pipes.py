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
        self.gap = randint(180,320)
        self.add(Pipe(self.width, self.gap, self.color, 0))
        self.add(Pipe(self.width, self.gap, self.color, 1))

    def update(self):
        self.counter -= 1
        if self.counter < 0:
            self.gap = randint(180,320)
            self.add(Pipe(self.width, self.gap, self.color, 0))
            self.add(Pipe(self.width, self.gap, self.color, 1))
            self.counter = self.width / self.density
        pygame.sprite.Group.update(self)