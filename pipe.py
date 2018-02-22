import pygame

class Pipe(pygame.sprite.Sprite):
    
    def __init__(self, x, y, color, direction, bird, gameState, playSounds):
        pygame.sprite.Sprite.__init__(self)
        self.playSounds = playSounds
        self.images = [ pygame.image.load('assets/sprites/pipe-red.png').convert_alpha(),
                        pygame.image.load('assets/sprites/pipe-green.png').convert_alpha() ]
        self.image = self.images[color]
        self.bird = bird
        self.gameState = gameState
        if direction == 1:
            self.image = pygame.transform.flip(self.image,0,1)
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.bottomleft = (x, y - 100)
        else:
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.topleft = (x, y)
        
    def update(self): # hitching, rewrite entire class later
        self.rect.move_ip(-1, 0)
        if self.rect.x < -52:
            self.kill()
        if(self.collide(self.bird)):
            self.playSounds[0](2)
            self.playSounds[0](3)
            self.gameState.set(2)

    def collide(self, other):
        offset = list((other.rect[0] - self.rect[0], other.rect[1] - self.rect[1]))
        return self.mask.overlap_area(other.mask, offset) != 0