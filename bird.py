import pygame
from globals import *
from random import randint

class Bird(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images_bases = [[pygame.image.load('assets/sprites/yellowbird-downflap.png').convert_alpha(),
                             pygame.image.load('assets/sprites/yellowbird-midflap.png').convert_alpha(),
                             pygame.image.load('assets/sprites/yellowbird-upflap.png').convert_alpha()],
                            [pygame.image.load('assets/sprites/redbird-downflap.png').convert_alpha(),
                             pygame.image.load('assets/sprites/redbird-midflap.png').convert_alpha(),
                             pygame.image.load('assets/sprites/redbird-upflap.png').convert_alpha()],
                            [pygame.image.load('assets/sprites/bluebird-downflap.png').convert_alpha(),
                             pygame.image.load('assets/sprites/bluebird-midflap.png').convert_alpha(),
                             pygame.image.load('assets/sprites/bluebird-upflap.png').convert_alpha()]]
        self.images_base = self.images_bases[randint(0,2)]
        self.angles = range(20, -80, -5)
        self.images = [[pygame.transform.rotate(image, angle) for image in self.images_base] for angle in self.angles]
        # 3 x 20 matrix with images for all positions
        # rows are for different wing poisitons
        # coloumns are for different angles

        self.masks = [[pygame.mask.from_surface(column) for column in row] for row in self.images]
        # precalculated masks
        self.rects = [[column.get_rect() for column in row] for row in self.images]
        # precalculated rects

        self.wing = 0
        self.angle = 0

        self.image = self.images[self.wing][self.angle]
        self.mask = self.masks[self.wing][self.angle]
        self.rect = self.rects[self.wing][self.angle]
        self.rect.center = (WIDTH // 2, 255)

        self.z = 0 #counter 


    
    def update(self):
        self.flap()
        if self.z > TICKRATE / 4:
            self.angle -= 1
            self.rect.move_ip(0, -180 / TICKRATE)
            self.z -= 1 
        elif self.z > TICKRATE / 6:
            self.rect.move_ip(0, -60 / TICKRATE)
            self.z -= 1
        elif self.z > 0:
            self.rect.move_ip(0, 120 / TICKRATE)
            self.z -= 1
        else:           
            self.rect.move_ip(0, 300 / TICKRATE)
            self.angle += 1
            self.z = 0
        
        if self.angle < 0:
            self.angle = 0
        elif self.angle > 19:
            self.angle = 19

        if  self.rect.y > 368: # calculation for floor collision, could be replaced with real colision
            PLAYSOUNDS[0](2)
            PLAYSOUNDS[0](3)
            GAMESTATE.set(2)

    def bounce(self):
        PLAYSOUNDS[0](0)
        self.z = TICKRATE / 2;

    def flap(self):
        self.wing += 1
        self.wing %= 3
        self.image = self.images[self.angle][self.wing]
        self.mask = self.masks[self.angle][self.wing]