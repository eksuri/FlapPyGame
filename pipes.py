import pygame
from globals import *
from pipe import Pipe
from random import randint

class Pipes(pygame.sprite.Group):
    
    def __init__(self, bird):
        pygame.sprite.Group.__init__(self)
        self.counter = 288 / PIPE_DENSITY
        self.color = randint(0,1)
        self.gap = randint(180,320)
        self.bird = bird
        self.add(Pipe(self.gap, self.color, 0, self.bird))
        self.add(Pipe(self.gap, self.color, 1, self.bird))

    def update(self):
        self.counter -= 1
        if self.counter < 0:
            self.gap = randint(180,320)
            self.add(Pipe(self.gap, self.color, 0, self.bird))
            self.add(Pipe(self.gap, self.color, 1, self.bird))
            self.counter = 288 / PIPE_DENSITY
        pygame.sprite.Group.update(self)