#      //\          
#     //  \         
#    //____\        
#   //      \       
#  //        \      
#
#
# Remember! Pygame (and python) is required to run this code. Please first install it before running.

import pygame
pygame.init()
studio = pygame.display.set_mode((600,600))
running = True

bg = pygame.image.load("C:\\Users\\Asrie\\Coding\\Python\\Advanced-Coding\\greetingcard\\minecraft base.png")
#Made from the server you will join (if you want to survive)
steve = pygame.image.load("C:\\Users\\Asrie\\Coding\\Python\\Advanced-Coding\\greetingcard\\steve.png")
#he's not big, he's just up close
font = pygame.font.SysFont("Determination Mono Web Regular",29)
text = font.render("Join the Server NOW! IP = 192.168.31.78",False,"#5E5E5E")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    studio.blit(bg,(-100,75))
    studio.blit(steve,(100,100))
    studio.blit(text,(10,10))

    pygame.display.update()