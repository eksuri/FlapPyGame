import pygame

class Overlay(pygame.sprite.Group):
    
    def __init__(self, width, height):
        pygame.sprite.Group.__init__(self)    
        self.width = width
        self.height = height
        

    def update(self):      
        pygame.sprite.Group.update(self)

        #if self.gameover:
        #    self.add(GameOver(self.width, self.height))