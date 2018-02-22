import pygame

class Score(pygame.sprite.Sprite):
    
    def __init__(self, int, position):
        pygame.sprite.Sprite.__init__(self)
        self.images = [ pygame.image.load('assets/sprites/0.png').convert_alpha(),
                        pygame.image.load('assets/sprites/1.png').convert_alpha(),
                        pygame.image.load('assets/sprites/2.png').convert_alpha(),
                        pygame.image.load('assets/sprites/3.png').convert_alpha(),
                        pygame.image.load('assets/sprites/4.png').convert_alpha(),
                        pygame.image.load('assets/sprites/5.png').convert_alpha(),
                        pygame.image.load('assets/sprites/6.png').convert_alpha(),
                        pygame.image.load('assets/sprites/7.png').convert_alpha(),
                        pygame.image.load('assets/sprites/8.png').convert_alpha(),
                        pygame.image.load('assets/sprites/9.png').convert_alpha() ]
        self.image = self.images[int]   
        self.rect = self.image.get_rect()
        self.rect.center = position