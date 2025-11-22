import pygame
from pygame.locals import *
pygame.init()
studio = pygame.display.set_mode((600,600))
running = True

bg = pygame.image.load("/var/home/phoenixerr/VSCodium/flyhacks/bg.png")
steve = pygame.image.load("/var/home/phoenixerr/VSCodium/flyhacks/steve.png")
stevex = 100
stevey = 100
keys = [False,False,False,False]
while stevey <= 600:
    studio.blit(bg, (0,0))
    studio.blit(steve, (100,100))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key==K_UP:
                keys[0]=True
            elif event.key==K_DOWN:
                keys[1]=True
            elif event.key==K_LEFT:
                keys[2]=True
            elif event.key==K_RIGHT:
                keys[3]=True

        if event.type == pygame.KEYUP:
            if event.key==K_UP:
                keys[0]=False
            elif event.key==K_DOWN:
                keys[1]=False
            elif event.key==K_LEFT:
                keys[2]=False
            elif event.key==K_RIGHT:
                keys[3]=False
    if keys[0]:
        if stevey >= 0:
            stevey -= 10