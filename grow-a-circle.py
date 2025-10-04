import pygame
pygame.init()
studio = pygame.display.set_mode((600,600))
running = True

class growcircle:
    def __init__(self,color,pos,radius,width):
        self.color = color
        self.pos = pos
        self.radius = radius
        self.width = width
        self.surface = studio
        
    def draw(self):
        self.draw_circle = pygame.draw.circle(self.surface,self.color,self.pos,self.radius,self.width)

    def grow(self,r):
        self.radius = self.radius+r
        self.draw_circle = pygame.draw.circle(self.surface,self.color,self.pos,self.radius,self.width)

circle = growcircle("#00830B",(350,350),30,9999)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            studio.fill("#000000")
            circle.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            studio.fill("#000000")
            circle.grow(10)
            pygame.display.update()