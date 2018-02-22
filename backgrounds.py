import pygame
from background import Background

class Backgrounds(pygame.sprite.Group):
    
    def __init__(self, width, height, daynight):
        pygame.sprite.Group.__init__(self)
        self.width = width
        self.daynight = daynight
        self.add(Background(self.width, self.width, self.daynight))
        self.add(Background(self.width, 0, self.daynight))

    def update(self):
        pygame.sprite.Group.update(self)