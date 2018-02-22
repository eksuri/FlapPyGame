import pygame
from globals import *

class Menu(pygame.sprite.Sprite):
    
    def __init__(self, int):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.image.load('assets/sprites/message.png').convert_alpha(),
                       pygame.image.load('assets/sprites/gameover.png').convert_alpha()]
        self.image = self.images[int]
        self.rect = self.image.get_rect()
        self.rect.center = ( WIDTH // 2, HEIGHT // 2)