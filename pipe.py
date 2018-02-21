import pygame

from random import randint

class Pipe:
    
    def __init__(self, width, int):
        self.width = width
        self.pipes = [[self.width + 120, randint(80, 320)],
                      [self.width + 240, randint(80, 320)],
                      [self.width + 360, randint(80, 320)]]
        self.sprites = [ pygame.image.load('assets/sprites/pipe-red.png').convert_alpha(),
                         pygame.image.load('assets/sprites/pipe-green.png').convert_alpha() ]
        self.bottom = self.sprites[int]
        self.top = pygame.transform.flip(self.bottom,0,1)

        

    def paint(self, DISPLAY): # hitching, rewrite entire class later
        if self.pipes[0][0] <= -52:
            self.pipes.append([self.width, randint(80, 320)]) #gap is because of
            self.pipes.pop(0)

        for pipe in self.pipes:
            DISPLAY.blit(self.bottom, (pipe[0], pipe[1]))
            DISPLAY.blit(self.top, (pipe[0], pipe[1] - 420))
            pipe[0] -= 1
        

    def getPosition(self):
        return self.pos
