import pygame

class Background(pygame.sprite.Sprite):
    
    def __init__(self, width, position, daynight):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.position = position
        self.images = [ pygame.image.load('assets/sprites/background-day.png').convert(),
                        pygame.image.load('assets/sprites/background-night.png').convert()]
        self.image = self.images[daynight]   
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.position, 0)

    def update(self):        
        self.position -= 1
        if self.position == -self.width:
            self.position = self.width
            self.rect.move_ip(2*self.width, 0)
        else:
            self.rect.move_ip(-1, 0)