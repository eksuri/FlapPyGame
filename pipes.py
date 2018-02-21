import pygame

class Pipes:
    
    def __init__(self, width, pos, int):
        self.z = 600
        self.pipes = []
        self.x = width
        self.pos = pos
        if int == 0:
            self.sprite = pygame.image.load('assets/sprites/pipe-green.png').convert_alpha()
        else:
            self.sprite = pygame.image.load('assets/sprites/pipe-red.png').convert_alpha()

    def paint(self, DISPLAY):
        self.x -= 1  
        self.z -= 1
        if self.z = 0:
            self.z += 120



        DISPLAY.blit(self.sprite, (self.x, self.pos))

    def getPosition(self):
        return self.pos
