import pygame
from globals import *
from bird import Bird
from random import randint

class Birds(pygame.sprite.Group):
    
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        self.add(Bird())

    def update(self):
        pygame.sprite.Group.update(self)

    def die(self):
        for bird in pygame.sprite.Group.sprites(self):
            bird.die()

    def getBird(self):
        for bird in pygame.sprite.Group.sprites(self):
            return bird