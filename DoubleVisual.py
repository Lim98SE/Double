# DGR-2
# memory range is (0, 0) - (255, 240)

import pygame
import os

global data

pygame.init()

draw = pygame.Surface((255, 240))
screen = pygame.display.set_mode((255*3,240*3))
pygame.display.set_caption("Double Screen")

pal = []

for B in range(3):
    for G in range(3):
        for R in range(3):
            pal.append((R * (255 // 2), G * (255 // 2), B * (255 // 2))) # Generates the pallate lmao

def tickScreen(data):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    for Y in range(240):
        for X in range(255):
            draw.set_at((X, Y), pal[data[X][Y]%len(pal)])

    screen.blit(pygame.transform.scale(draw, screen.get_rect().size), (0,0)) # big
    
    pygame.display.update()
