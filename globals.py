import pygame
from pygame import mixer
from grouplist import GroupList
from gamestate import GameState

global WIDTH, HEIGHT, TICKRATE, WINGSPEED, PIPE_DENSITY, PIPEGAP_FIXED, PIPEGAP_MIN, PIPEGAP_MAX, TITLE, CLOCK, DISPLAY, PLAYSOUNDS, GAMESTATE, GROUPS

pygame.init()

##settings to change: ###########################
#
WIDTH = 320 # try it widescreen!
HEIGHT = 512 # don't change
TICKRATE = 20 # variable, 20-120
WINGSPEED = 20 # tickrate floor
#10*40 = Terminal * 6.666 # bounce velocity
#1*40 = Terminal * .66666# gravity
#20*40 = Terminal * 13.3333 # terminal velocity
#
PIPE_DENSITY = 3 # variable
PIPE_BUFFER = 80 # how far off the floor / roof the pipe has to be 
PIPEGAP_FIXED = False
PIPEGAP_MIN = 80 # if fixed = true, uses minimum
PIPEGAP_MAX = 160 # how large the gap between the two pipes can be
#
ZBACKGROUNDS = 0 # 0 = random, 1 = day, 2 = night
ZBIRDS = 0 # 0 = random, 1 = yellow, 2 = red, 3 = blue
ZPIPES = 0 # 0 = random, 1 = green, 2 = red
#
TITLE = 'Flappy Bird'
#
#################################################


CLOCK = pygame.time.Clock()
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))

sounds = [mixer.Sound("assets/audio/wing.wav"),
          mixer.Sound("assets/audio/point.ogg"),
          mixer.Sound("assets/audio/hit.ogg"),
          mixer.Sound("assets/audio/die.ogg"),
          mixer.Sound("assets/audio/swoosh.ogg")]

def play(int):
    sounds[int].play(0)

PLAYSOUNDS = [play] # allows callbacks
GROUPS = GroupList()
GAMESTATE = GameState(GROUPS)
