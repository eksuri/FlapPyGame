import pygame

class Bird(pygame.sprite.Sprite):
    
    def __init__(self, int):
        pygame.sprite.Sprite.__init__(self)
        if int == 0:
            self.images = [pygame.image.load('assets/sprites/yellowbird-downflap.png').convert_alpha(),
                           pygame.image.load('assets/sprites/yellowbird-midflap.png').convert_alpha(),
                           pygame.image.load('assets/sprites/yellowbird-upflap.png').convert_alpha()]
        elif int == 1:
            self.images = [pygame.image.load('assets/sprites/redbird-downflap.png').convert_alpha(),
                           pygame.image.load('assets/sprites/redbird-midflap.png').convert_alpha(),
                           pygame.image.load('assets/sprites/redbird-upflap.png').convert_alpha()]
        else:
            self.images = [pygame.image.load('assets/sprites/bluebird-downflap.png').convert_alpha(),
                           pygame.image.load('assets/sprites/bluebird-midflap.png').convert_alpha(),
                           pygame.image.load('assets/sprites/bluebird-upflap.png').convert_alpha()]

        self.image = self.images[1]
        self.rect = self.image.get_rect()
        self.rect.center = (80, 255)
        self.z = 0 #counter 

    
    def update(self):
        if self.z > 20:
            self.rect.move_ip(0, -2)
            self.z -= 1
            self.image = self.images[1]   
        elif self.z > 10:
            self.rect.move_ip(0, -2)
            self.z -= 1
            self.image = self.images[2]
        elif self.z > 0:
            self.rect.move_ip(0, 0)
            self.z -= 1
            self.image = self.images[1]
        else:           
            self.rect.move_ip(0, 3)
            self.z = 0
            self.image = self.images[0]
        
        #if self.y < 0:
        #    self.y = 0
        #elif self.y > 376:
        #    self.y = 376

    def bounce(self):
        self.z = 30;

    #def getPosition(self):

    #def die(self):