import pygame

class Background(pygame.sprite.Sprite):
    
    def __init__(self, position, daynight):
        pygame.sprite.Sprite.__init__(self)
        self.images = [ pygame.image.load('assets/sprites/background-day.png').convert(),
                        pygame.image.load('assets/sprites/background-night.png').convert()]
        self.image = self.images[daynight]   
        self.rect = self.image.get_rect()
        self.rect.topleft = (position, 0)