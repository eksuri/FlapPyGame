import pygame

class Bird:
    
    def __init__(self, int):
        self.x = 80
        self.y = 255
        if int == 0:
            self.sprite = [pygame.image.load('assets/sprites/yellowbird-downflap.png').convert_alpha(),
                           pygame.image.load('assets/sprites/yellowbird-midflap.png').convert_alpha(),
                           pygame.image.load('assets/sprites/yellowbird-upflap.png').convert_alpha()]
        elif int == 1:
            self.sprite = [pygame.image.load('assets/sprites/redbird-downflap.png').convert_alpha(),
                           pygame.image.load('assets/sprites/redbird-midflap.png').convert_alpha(),
                           pygame.image.load('assets/sprites/redbird-upflap.png').convert_alpha()]
        else:
            self.sprite = [pygame.image.load('assets/sprites/bluebird-downflap.png').convert_alpha(),
                           pygame.image.load('assets/sprites/bluebird-midflap.png').convert_alpha(),
                           pygame.image.load('assets/sprites/bluebird-upflap.png').convert_alpha()]

        self.z = 0 #counter 

    
    def paint(self, DISPLAY):
        if self.z > 20:
            self.y -= 2
            self.z -= 1
            sprite =  self.sprite[1]    
        elif self.z > 10:
            self.y -= 1
            self.z -= 1
            sprite = self.sprite[2]
        elif self.z > 0:
            self.y -= 0
            self.z -= 1
            sprite = self.sprite[1]
        else:           
            self.y += 3
            self.z = 0
            sprite = self.sprite[0]
        
        if self.y < 0:
            self.y = 0
        elif self.y > 376:
            self.y = 376

        DISPLAY.blit(sprite, (self.x, self.y))

    def bounce(self):
        self.z = 30;

    def getPosition(self):
        return self.y

    def die(self):
        self.y = 0