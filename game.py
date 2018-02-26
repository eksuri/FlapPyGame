import pygame
from pygame import mixer
from globals import *

from backgrounds import Backgrounds
from birds import Birds
from grounds import Grounds
from grouplist import GroupList
from menu import Menu
from pipes import Pipes
from scores import Scores

from random import randint
    
def main():

    pygame.display.set_caption(TITLE)
    crashed = False

    while not crashed:
        if GAMESTATE.changed():
            if GAMESTATE.get() == 0:
                backgroundGroup = Backgrounds()
                groundGroup = Grounds()
                menuGroup = pygame.sprite.Group(Menu(0))

                GROUPS.add(backgroundGroup, groundGroup, menuGroup)

            elif GAMESTATE.get() == 1:
                birdGroup = Birds()
                backgroundGroup = Backgrounds()
                pipeGroup = Pipes(birdGroup.getBird())
                groundGroup = Grounds()
                scoreGroup = Scores()

                GROUPS.add(backgroundGroup, pipeGroup, groundGroup, birdGroup, scoreGroup)  

            elif GAMESTATE.get() == 2:
                menuGroup = pygame.sprite.Group(Menu(1))

                GROUPS.add(menuGroup)
            else:
                crashed = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                if GAMESTATE.get() == 0:
                    GAMESTATE.set(1)
                elif GAMESTATE.get() == 1:
                    birdGroup.getBird().bounce()
                elif GAMESTATE.get() == 2:
                    GAMESTATE.set(0)
                else:
                    crash = True


        GROUPS.update()
        GROUPS.draw(DISPLAY)

        pygame.display.update()   
        CLOCK.tick(TICKRATE)

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()