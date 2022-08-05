# DGR-3

import pygame
import os

global data

pygame.init()

res = 64
scale = 10

screen = pygame.display.set_mode((res*scale,res*scale))
pygame.display.set_caption("Double Screen")

pal = []

depth = 4

for B in range(depth):
    for G in range(depth):
        for R in range(depth):
            pal.append((R * (255 // depth - 1), G * (255 // depth - 1), B * (255 // depth - 1))) # Generates the pallate lmao

def tickScreen(data):

    draw = pygame.Surface((res, res))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    for Y in range(res):
        for X in range(res):
            draw.set_at((X, Y), pal[data[X][Y]%len(pal)])

    screen.blit(pygame.transform.scale(draw, (res*scale, res*scale)), (0,0)) # big
    
    pygame.display.update()
