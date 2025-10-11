import pygame
pygame.init()
studio = pygame.display.set_mode((600,600))
running = True

class Growrect:
    def __init__(self,color,x,y,sizex,sizey,width):
        self.color = color
        self.x = x
        self.y = y
        self.sizex = sizex
        self.sizey = sizey
        self.width = width
        self.surface = studio
        
    def draw(self):
        self.draw_rect = pygame.draw.rect(self.surface,self.color,(self.x, self.y, self.sizex, self.sizey))

    def grow(self,r,t):
        self.sizex += r
        self.sizey += t
        self.draw_rect = pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.sizex, self.sizey))

recta = Growrect("#00830B",0,0,30,30,9999)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            studio.fill("#000000")
            recta.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            studio.fill("#000000")
            recta.grow(10,10)
            pygame.display.update()