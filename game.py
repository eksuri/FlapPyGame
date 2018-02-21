import pygame
from background import Background
from bird import Bird
from pipe import Pipe
from ground import Ground
from overlay import Overlay

from random import randint

WIDTH = 288
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

    bg = Background(randint(0,1))
    br = Bird(randint(0,2))
    pp = Pipe(WIDTH, randint(0,1))
    gr = Ground()
    ol = Overlay()

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            elif event.type == pygame.KEYDOWN:
                br.bounce()

        bg.paint(DISPLAY)
        br.paint(DISPLAY)
        pp.paint(DISPLAY)
        gr.paint(DISPLAY)
        ol.paint(DISPLAY)
    
        pygame.display.update()
        CLOCK.tick(TICKRATE)

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()