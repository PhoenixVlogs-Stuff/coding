import pygame
pygame.init()
studio = pygame.display.set_mode((600,600))
running = True
PYGAME_DETECT_AVX2=1
keys = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            studio.fill("#51B400")
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            studio.fill("#000000")
            pygame.display.update()
    
