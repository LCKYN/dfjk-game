import pygame
import config

size = config.size
scale = config.scale
color = config.color

pygame.init()

screen = pygame.display.set_mode([size["x"], size["y"]])
clock = pygame.time.Clock()

count = 30

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

    pygame.draw.rect(screen, color["box"], pygame.Rect(10, 10, 105, count))
    count += 1

    pygame.display.flip()
    pygame.display.update()

    clock.tick(40)

pygame.quit()
