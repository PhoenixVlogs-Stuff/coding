import pygame
pygame.init()
studio = pygame.display.set_mode((600,600))
class Rectangle:
    def __init__(self,color,dimensions):
        self.screen = studio
        self.rect_color = color
        self.rect_dimensions = dimensions
    def draw(self):
        pygame.draw.rect(self.screen,self.rect_color,self.rect_dimensions)
green = Rectangle("#065D00",(100,100,50,30))
orange = Rectangle("#E09500",(100,130,30,70))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    studio.fill("#202020")
    green.draw()
    orange.draw()
    pygame.display.update()