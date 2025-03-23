import pygame
import pyscroll
import pytmx
import os
import main
pygame.init()
screen, surface = pygame.display.set_mode((720,500)), pygame.Surface((100,100))
x, y = 150, 200
timer = pygame.time.Clock()
game_on = True
while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame.mouse.get_pressed
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        x -= 1
    if pressed[pygame.K_RIGHT]:
        x += 1
    if pressed[pygame.K_UP]:
        y -= 1
    if pressed[pygame.K_DOWN]:
        y += 1
    
    screen.fill(pygame.Color("blue"))
    surface.fill((36, 107, 255))
    screen.blit(surface, (x, y))
    
    pygame.display.flip()
    timer.tick(144)
pygame.quit()