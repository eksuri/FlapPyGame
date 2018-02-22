import pygame

from gamestate import GameState

class Bird(pygame.sprite.Sprite):
    
    def __init__(self, int, gameState, playSounds):
        pygame.sprite.Sprite.__init__(self)
        self.gameState = gameState
        self.playSounds = playSounds
        if int == 0:
            self.images_base = [pygame.image.load('assets/sprites/yellowbird-downflap.png').convert_alpha(),
                           pygame.image.load('assets/sprites/yellowbird-midflap.png').convert_alpha(),
                           pygame.image.load('assets/sprites/yellowbird-upflap.png').convert_alpha()]
        elif int == 1:
            self.images_base = [pygame.image.load('assets/sprites/redbird-downflap.png').convert_alpha(),
                           pygame.image.load('assets/sprites/redbird-midflap.png').convert_alpha(),
                           pygame.image.load('assets/sprites/redbird-upflap.png').convert_alpha()]
        else:
            self.images_base = [pygame.image.load('assets/sprites/bluebird-downflap.png').convert_alpha(),
                           pygame.image.load('assets/sprites/bluebird-midflap.png').convert_alpha(),
                           pygame.image.load('assets/sprites/bluebird-upflap.png').convert_alpha()]

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
        self.rect.center = (80, 255)

        self.z = 0 #counter 


    
    def update(self):
        self.flap()
        if self.z > 15:
            self.angle -= 1
            self.rect.move_ip(0, -3)
            self.z -= 1 
        elif self.z > 10:
            self.rect.move_ip(0, -1)
            self.z -= 1
        elif self.z > 0:
            self.rect.move_ip(0, 2)
            self.z -= 1
        else:           
            self.rect.move_ip(0, 5)
            self.angle += 1
            self.z = 0
        
        if self.angle < 0:
            self.angle = 0
        elif self.angle > 19:
            self.angle = 19

        if  self.rect.y > 368: # calculation for floor collision, could be replaced with real colision
            self.playSounds[0](2)
            self.playSounds[0](3)
            self.gameState.set(2)

    def bounce(self):
        self.playSounds[0](0)
        self.z = 30;

    def flap(self):
        self.wing += 1
        self.wing %= 3
        self.image = self.images[self.angle][self.wing]
        self.mask = self.masks[self.angle][self.wing]

    #def getPosition(self):

    #def die(self):