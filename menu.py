import pygame

class Menu(pygame.sprite.Sprite):
    
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/sprites/message.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, height/2)