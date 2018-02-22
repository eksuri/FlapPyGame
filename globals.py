import pygame
from pygame import mixer
from grouplist import GroupList
from gamestate import GameState

global WIDTH, HEIGHT, TICKRATE, PIPE_DENSITY, TITLE, CLOCK, DISPLAY, PLAYSOUNDS, GAMESTATE, GROUPS

pygame.init()

WIDTH = 1024 # variable
HEIGHT = 512 # fixed
TICKRATE = 60 # fixed... for now
PIPE_DENSITY = 2 # variable
TITLE = 'Flappy Bird'

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
