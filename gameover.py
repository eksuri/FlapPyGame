import pygame

class GameOver(pygame.sprite.Sprite):
    
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/sprites/gameover.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, height/2)