import pygame

class Overlay:
    
    def __init__(self):
        self.gameover = pygame.image.load('assets/sprites/gameover.png').convert_alpha()
        self.gameover = False    

    def paint(self, DISPLAY):        
        if self.gameover:
            DISPLAY.blit(self.gameover, (100, 125))