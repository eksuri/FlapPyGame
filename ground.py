import pygame

class Ground(pygame.sprite.Sprite):
    
    def __init__(self, width, position):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.position = position
        self.image = pygame.image.load('assets/sprites/base.png').convert() 
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.position, 400) 

    def update(self):        
        self.position -= 1
        if self.position == -self.width:
            self.position = self.width
            self.rect.move_ip(2*self.width, 0)
        self.rect.move_ip(-1, 0)