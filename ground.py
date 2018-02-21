import pygame

class Ground:
    
    def __init__(self):
        self.ground = pygame.image.load('assets/sprites/base.png').convert() 
        self.x = 0    

    def paint(self, DISPLAY):        
        self.x -= 1
        self.x = self.x % 337
        DISPLAY.blit(self.ground, (self.x, 400))
        DISPLAY.blit(self.ground, (self.x - 336, 400))
