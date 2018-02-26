import pygame
from globals import *
from random import randint

class Pipe(pygame.sprite.Sprite):
    
    def __init__(self, y, color, direction, bird):
        pygame.sprite.Sprite.__init__(self)
        self.images = [ pygame.image.load('assets/sprites/pipe-red.png').convert_alpha(),
                        pygame.image.load('assets/sprites/pipe-green.png').convert_alpha() ]
        self.image = self.images[color]
        self.bird = bird
        self.direction = direction
        self.middle = WIDTH // 2
        self.alive = True 

        if direction == 1:
            self.image = pygame.transform.flip(self.image,0,1)
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            if not PIPEGAP_FIXED:
                self.rect.bottomleft = (WIDTH, y - randint(PIPEGAP_MIN, PIPEGAP_MAX))
            else:
                self.rect.bottomleft = (WIDTH, y - PIPEGAP_MIN)
        else:
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.topleft = (WIDTH, y)
        
    def update(self):
        self.rect.move_ip(-120 / TICKRATE, 0)
        if self.rect.x == self.middle and self.direction == 0:
            PLAYSOUNDS[0](1)
            GAMESTATE.score()

        if self.rect.x < -52:
            self.kill()
        if(self.alive and self.collide(self.bird)):
            PLAYSOUNDS[0](2)
            PLAYSOUNDS[0](3)
            GAMESTATE.set(2)

    def die(self):
        self.alive = False

    def collide(self, other):
        offset = list((other.rect[0] - self.rect[0], other.rect[1] - self.rect[1]))
        return self.mask.overlap_area(other.mask, offset) != 0