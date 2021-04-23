import pygame
pygame.font.init()
font = pygame.font.Font('font/MesloLGS NF Regular.ttf', 32)

class Score:
    def __init__(self):
        self.amount = 0
    
    def add(self, n):
        self.amount += n
    
    def show(self):
        return font.render("{socre}".format(socre = self.amount), True, (0,0,0))
