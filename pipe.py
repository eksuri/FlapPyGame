import pygame

class Pipe(pygame.sprite.Sprite):
    
    def __init__(self, x, y, color, direction):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.images = [ pygame.image.load('assets/sprites/pipe-red.png').convert_alpha(),
                        pygame.image.load('assets/sprites/pipe-green.png').convert_alpha() ]
        self.image = self.images[color]
        if direction == 1:
            self.image = pygame.transform.flip(self,0,1)
            self.rect = self.image.get_rect()
            self.rect.center = (200, 0)
        else:
            self.rect = self.image.get_rect()
            self.rect.center = (200, 255)
        
    def update(self): # hitching, rewrite entire class later
        self.rect.move_ip(-1, 0)
