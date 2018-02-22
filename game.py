import pygame

from grouplist import GroupList
from backgrounds import Backgrounds
from bird import Bird
from pipes import Pipes
from grounds import Grounds
from overlay import Overlay

from random import randint

WIDTH = 1024 # variable
HEIGHT = 512 # fixed
TICKRATE = 60 # variable
PIPE_DENSITY = 2 # variable
TITLE = 'Flappy Bird'

pygame.init()
    
def main():
    pygame.init()
    pygame.display.set_caption(TITLE)

    global CLOCK, DISPLAY
    CLOCK = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))

    crashed = False

    br = Bird(randint(0,2))
    birdGroup = pygame.sprite.Group((br))
    backgroundGroup = Backgrounds(WIDTH, randint(0,1))
    pipeGroup = Pipes(WIDTH, PIPE_DENSITY, randint(0,1))
    groundGroup = Grounds(WIDTH)
    overlayGroup = Overlay(WIDTH, HEIGHT)

    groups = GroupList()    
    groups.add(backgroundGroup, birdGroup, pipeGroup, groundGroup)

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            elif event.type == pygame.KEYDOWN:
                br.bounce()


        groups.update()
        groups.draw(DISPLAY)

        pygame.display.update()   
        CLOCK.tick(TICKRATE)

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()