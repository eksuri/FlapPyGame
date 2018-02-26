import pygame
from globals import *
from background import Background
from random import randint

class Backgrounds(pygame.sprite.Group):
    
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        if ZBACKGROUNDS == 0:
            self.daynight = randint(0,1)
        else:
            self.daynight = ZBACKGROUNDS - 1
        for x in range(0, WIDTH, 288):
            self.add(Background(x, self.daynight))

    def update(self):
        pygame.sprite.Group.update(self)


    def die(self):
        pass