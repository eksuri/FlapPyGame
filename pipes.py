import pygame
from globals import *
from pipe import Pipe
from random import randint

class Pipes(pygame.sprite.Group):
    
    def __init__(self, bird):
        pygame.sprite.Group.__init__(self)
        self.counter = 288 / PIPE_DENSITY
        if ZPIPES == 0:
            self.color = randint(0,1)
        else:
            self.color = ZPIPES - 1
        self.gap = randint(PIPEGAP_MIN + PIPE_BUFFER, 400 - PIPE_BUFFER)
        self.bird = bird
        self.add(Pipe(self.gap, self.color, 0, self.bird))
        self.add(Pipe(self.gap, self.color, 1, self.bird))

    def update(self):
        self.counter -= 60 / TICKRATE
        if self.counter < 0:
            self.gap = randint(PIPEGAP_MIN + PIPE_BUFFER, 400 - PIPE_BUFFER)
            self.add(Pipe(self.gap, self.color, 0, self.bird))
            self.add(Pipe(self.gap, self.color, 1, self.bird))
            self.counter = 288 / PIPE_DENSITY
        pygame.sprite.Group.update(self)