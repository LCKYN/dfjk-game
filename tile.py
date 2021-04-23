import pygame

import config

color = config.color
scale = config.scale
size_tile = config.size_tile

class Tile:
    def __init__(self, lane):
        self.lane = lane
        self.y = -30
        self.hit = False
    
    def update(self, bpm):
        self.y += bpm

    def get_hit(self):
        self.hit = True

    def draw(self, surface):
        if(not hit):
            rect = pygame.Rect(10 + scale["v_line"] * self.lane, self.y, size_tile["x"], size_tile["y"])
            pygame.draw.rect(surface, color["tile"], rect)