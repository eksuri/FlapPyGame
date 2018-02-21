import pygame

class Background:
    
    def __init__(self, int):
        self.backgrounds = [ pygame.image.load('assets/sprites/background-day.png').convert(),
                             pygame.image.load('assets/sprites/background-night.png').convert()]
        self.background = self.backgrounds[int]   
        self.x = 0    

    def paint(self, DISPLAY):        
        self.x += 1
        self.x = self.x % 289
        DISPLAY.blit(self.background, (self.x - 289, 0))
        DISPLAY.blit(self.background, (self.x, 0))
