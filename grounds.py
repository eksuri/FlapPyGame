import pygame
from ground import Ground

class Grounds(pygame.sprite.Group):
    
    def __init__(self, width):
        pygame.sprite.Group.__init__(self)
        self.width = 336
        self.add(Ground(self.width, self.width))
        self.add(Ground(self.width, 0))

    def update(self):
        pygame.sprite.Group.update(self)