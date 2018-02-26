import pygame
from grouplist import GroupList

class GameState:
    
    def __init__(self, groups):
        self.state = 0
        self.points = 0
        self.dirty = True
        self.groups = groups
    
    def set(self, i):
        self.state = i
        self.dirty = True
        if i == 2:
            self.groups.die()
        else:
            self.points = 0
            self.groups.empty()

    def get(self):
        self.dirty = False
        return self.state

    def changed(self):
        return self.dirty
        
    def score(self):
        self.points += 1

    def getScore(self):
        return self.points