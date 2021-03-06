import pygame
from globals import *
from score import Score

class Scores(pygame.sprite.Group):
    
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        self.middle = WIDTH // 2 # 30 appart
        self.height = 20
        self.score = 0
        self.add(Score(0, ( self.middle - 15, self.height)))
        self.add(Score(0, ( self.middle + 15, self.height)))

    def update(self):
        pygame.sprite.Group.update(self)
        self.score = GAMESTATE.getScore()
        self.empty()
        self.add(Score(self.score // 10, ( self.middle - 15, self.height)))
        self.add(Score(self.score % 10, ( self.middle + 15, self.height)))
    
    def die(self):
        pass