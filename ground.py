import pygame
from globals import *

class Ground(pygame.sprite.Sprite):
    
    def __init__(self, width, position, count):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/sprites/base.png').convert_alpha() 
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.position = position
        self.rect.topleft = (self.position, 400) 
        self.width = width # width of single tile
        self.start = count * width # width of all tiles
        self.alive = True

    def update(self):   
        if self.alive:     
            self.position -= 120 / TICKRATE
            if self.position == -self.width:
                self.position += self.start
                self.rect.move_ip(self.start, 0)
            self.rect.move_ip(-120 / TICKRATE, 0)
    
    def die(self):
        self.alive = False
        