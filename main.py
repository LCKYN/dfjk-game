import pygame
import random

import config
from tile import Tile



size = config.size
scale = config.scale
color = config.color

pygame.init()

screen = pygame.display.set_mode([size["x"], size["y"]])
clock = pygame.time.Clock()

count = 30


r = random.randint(0,4)
test_tile = Tile(r)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # draw background
    for i in range(1, 4):
        pygame.draw.line(screen, color["line"],
                         (i * scale["v_line"], 0), (i * scale["v_line"], size["y"]), scale["v_line_size"])
    pygame.draw.line(screen, color["line"],
                     (0, scale["h_line"]), (size["x"], scale["h_line"]), scale["h_line_size"])

    
    test_tile.update(5)
    test_tile.draw(screen)
    
    
    # pygame.draw.rect(screen, color["box"], pygame.Rect(135, 10, 105, 30))
    # pygame.draw.rect(screen, color["box"], pygame.Rect(260, 10, 105, 30))
    # pygame.draw.rect(screen, color["box"], pygame.Rect(385, 10, 105, 30))
    count += 1

    pygame.display.flip()
    pygame.display.update()

    clock.tick(60)

pygame.quit()
