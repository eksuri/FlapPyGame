import pygame
from pygame import mixer

from gamestate import GameState
from grouplist import GroupList
from backgrounds import Backgrounds
from bird import Bird
from pipes import Pipes
from grounds import Grounds
from menu import Menu
from gameover import GameOver

from random import randint

WIDTH = 336 # variable
HEIGHT = 512 # fixed
TICKRATE = 60 # fixed... for now
PIPE_DENSITY = 2 # variable
TITLE = 'Flappy Bird'

pygame.init()
    
def main():
    
    mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
    pygame.init()
    print(pygame.mixer.get_init())
    pygame.display.set_caption(TITLE)
   
    global CLOCK, DISPLAY
    CLOCK = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))

    groups = GroupList()
    gameState = GameState(groups) # 0 = menu, 1 = game, 2 = gameover, 3 = exit
    crashed = False

    sounds = [mixer.Sound("assets/audio/wing.ogg"),
              mixer.Sound("assets/audio/point.ogg"),
              mixer.Sound("assets/audio/hit.ogg"),
              mixer.Sound("assets/audio/die.ogg"),
              mixer.Sound("assets/audio/swoosh.ogg")]

    while not crashed:
        if gameState.changed():
            if gameState.get() == 0:
                backgroundGroup = Backgrounds(WIDTH, 0)
                groundGroup = Grounds(WIDTH)
                menuGroup = pygame.sprite.Group(Menu(WIDTH, HEIGHT))

                groups.add(backgroundGroup, groundGroup, menuGroup)

            elif gameState.get() == 1:
                br = Bird(randint(0,2), gameState)
                birdGroup = pygame.sprite.Group((br))
                backgroundGroup = Backgrounds(WIDTH, randint(0,1))
                pipeGroup = Pipes(WIDTH, PIPE_DENSITY, randint(0,1), br, gameState)
                groundGroup = Grounds(WIDTH)
                #scoreGroup = Scores(WIDTH, HEIGHT)

                groups.add(backgroundGroup, pipeGroup, groundGroup, birdGroup)  

            elif gameState.get() == 2:
                sounds[2].play(0)
                sounds[3].play(0)
                gameoverGroup = pygame.sprite.Group(GameOver(WIDTH, HEIGHT))
                #scoreGroup = Scores(WIDTH, HEIGHT)

                groups.add(backgroundGroup, groundGroup, gameoverGroup)
            else:
                crashed = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            elif event.type == pygame.KEYDOWN:
                if gameState.get() == 0: # could be dangerous...
                    gameState.set(1)
                elif gameState.get() == 1:
                    sounds[0].play(0)
                    br.bounce()
                elif gameState.get() == 2:
                    gameState.set(0)
                else:
                    crash = True


        groups.update()
        groups.draw(DISPLAY)

        pygame.display.update()   
        CLOCK.tick(TICKRATE)

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()