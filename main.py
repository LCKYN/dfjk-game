import pygame
import config


pygame.init()

screen = pygame.display.set_mode([config.size['x'], config.size['y']])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # draw background
    for i in range(1,4):
        pygame.draw.line(screen, (0, 0, 0), (i*125,0), (i*125,1000), 1)

    pygame.display.flip()
pygame.quit()