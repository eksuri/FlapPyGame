import pygame
from background import Background

class Backgrounds(pygame.sprite.Group):
    
    def __init__(self, width, daynight):
        pygame.sprite.Group.__init__(self)
        for x in range(0, width, 288):
            self.add(Background(x, daynight))

    def update(self):
        pygame.sprite.Group.update(self)