import pygame
pygame.init()
studio = pygame.display.set_mode((600,600))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    studio.fill("#065D00")
    pygame.display.update()