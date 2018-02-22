import pygame

class Ground(pygame.sprite.Sprite):
    
    def __init__(self, width, position, count):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.position = position
        self.start = count * width
        self.image = pygame.image.load('assets/sprites/base.png').convert() 
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.position, 400) 

    def update(self):        
        self.position -= 1
        if self.position == -self.width:
            self.position = self.start
            self.rect.move_ip(self.start, 0)
        self.rect.move_ip(-1, 0)