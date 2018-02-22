import pygame

class GroupList():
    
    def __init__(self):
        self.groupList = []
        
    def add(self, *groups):
        for group in groups:
            self.groupList.append(group)

    def update(self):
        for group in self.groupList:
            group.update()

    def draw(self, display):
        for group in self.groupList:
            group.draw(display)

    def empty(self):
        for group in self.groupList:
            group.empty()
        self.groupList = []

        