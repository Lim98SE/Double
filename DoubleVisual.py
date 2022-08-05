# DGR-1

import pygame
import os

global data

pygame.init()

draw = pygame.Surface((256//4, 256//4))
screen = pygame.display.set_mode((256*3,256*3))
pygame.display.set_caption("Double Screen")

pal = []

for R in range(5):
    for G in range(5):
        for B in range(5):
            pal.append((R * 63, G * 63, B * 63))

def tickScreen(data):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    for Y in range(255//4):
        for X in range(255//4):
            draw.set_at((X, Y), pal[data[X][Y]%len(pal)])

    screen.blit(pygame.transform.scale(draw, screen.get_rect().size), (0,0))
    
    pygame.display.update()
