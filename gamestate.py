import pygame
from grouplist import GroupList

class GameState:
    
    def __init__(self, groups):
        self.state = 0
        self.dirty = True
        self.groups = groups
    
    def set(self, i):
        self.state = i
        self.dirty = True
        self.groups.empty()

    def get(self):
        self.dirty = False
        return self.state

    def changed(self):
        return self.dirty