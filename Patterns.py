import random
import pgzrun
WIDTH = 720
HEIGHT = 540
TITLE = "Patterns - Version 1.0"
def draw():
    screen.fill("#000000")
    w = 264
    h = 286
    for i in range(15):
        R1 = Rect((0,0),(w,h))
        R1.center = (WIDTH/2,HEIGHT/2)
        R = 255
        G = 0
        B = random.randint(120,255)
        screen.draw.rect(R1,(R,G,B))
        blocks = 147
        screen.draw.circle((200,200),(blocks),(3,255,B))
        w -= 10
        h += 11
        blocks -= 14
pgzrun.go()