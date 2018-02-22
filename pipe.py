import pygame

class Pipe(pygame.sprite.Sprite):
    
    def __init__(self, x, y, color, direction):
        pygame.sprite.Sprite.__init__(self)
        self.images = [ pygame.image.load('assets/sprites/pipe-red.png').convert_alpha(),
                        pygame.image.load('assets/sprites/pipe-green.png').convert_alpha() ]
        self.image = self.images[color]
        if direction == 1:
            self.image = pygame.transform.flip(self.image,0,1)
            self.rect = self.image.get_rect()
            self.rect.bottomleft = (x, y - 100)
        else:
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
        
    def update(self): # hitching, rewrite entire class later
        self.rect.move_ip(-1, 0)
        if self.rect.x < -52:
            self.kill()
