import pygame
import random

import config
from tile import Tile
from score import Score



size = config.size
scale = config.scale
color = config.color

pygame.init()

screen = pygame.display.set_mode([size["x"], size["y"]])
clock = pygame.time.Clock()

count = 30

socre = 0


s = Score()

r = random.randint(0,4)
test_tile = Tile(r)

running = True

def check_hit(l):
    if(test_tile.get_hit(l)):
        s.add(100)
    else:
        s.add(-100)

def show_score():
    screen.blit(s.show(),(0,0))

def draw_background():
    for i in range(1, 4):
        pygame.draw.line(screen, color["line"],
                         (i * scale["v_line"], 0), (i * scale["v_line"], size["y"]), scale["v_line_size"])
    pygame.draw.line(screen, color["line"],
                     (0, scale["h_line"]), (size["x"], scale["h_line"]), scale["h_line_size"])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                check_hit(0)
            elif event.key == pygame.K_f:
                check_hit(1)
            elif event.key == pygame.K_j:
                check_hit(2)
            elif event.key == pygame.K_k:
                check_hit(3)

    screen.fill((255, 255, 255))
    
    draw_background()
    show_score()
    
    test_tile.update(5)
    test_tile.draw(screen)

    pygame.display.flip()
    pygame.display.update()

    clock.tick(60)

pygame.quit()