import pygame

from grouplist import GroupList
from backgrounds import Backgrounds
from bird import Bird
from pipes import Pipes
from ground import Ground
from overlay import Overlay

from random import randint

WIDTH = 290
HEIGHT = 512
TICKRATE = 60
TITLE = 'Flappy Bird'

pygame.init()
    
def main():
    pygame.init()
    pygame.display.set_caption(TITLE)

    global CLOCK, DISPLAY
    CLOCK = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))

    crashed = False

    backgroundGroup = Backgrounds(WIDTH, HEIGHT, randint(0,1))
    br = Bird(randint(0,2))
    gl = GroupList()
    birdGroup = pygame.sprite.Group((br))
    pipeGroup = Pipes(WIDTH, 3, randint(0,1))
    
    gl.add(backgroundGroup, birdGroup, pipeGroup)

    gr = Ground()
    ol = Overlay()
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            elif event.type == pygame.KEYDOWN:
                br.bounce()


        gl.update()
        gl.draw(DISPLAY)

        pygame.display.update()   
        CLOCK.tick(TICKRATE)

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()