import pgzrun
import random
from time import time
TITLE = "Untitled Line Game - Version infdev"
WIDTH = 720
HEIGHT = 540
startime = 0
endtime = 0
totaltime = 0
boxes = []
lines = []
nextbox = 0
total = 9
def boxlines():
    global startime
    for i in range(total):
        global box
        box = Actor("box")
        box.pos = random.randint(80,640),random.randint(50,490)
        boxes.append(box)
    startime = time()
def draw():
    global totaltime
    screen.blit("factory", (0,0))
    boxnumber = 1
    for e in boxes:
        screen.draw.text(str(boxnumber),(e.pos[0],e.pos[1]+30),color = "#00E900")
        e.draw()
        boxnumber += 1
    for o in lines:
        screen.draw.line(o[0],o[1],color = "#0062D1")
    if nextbox < total:
        totaltime = time() - startime
        screen.draw.text(str(round(totaltime,1)),(0,400))
    else:
        screen.draw.text(str(round(totaltime,1)),(0,400))
def update():
    pass
def on_mouse_down(pos):
    global nextbox, total, lines
    if nextbox < total:
        if boxes[nextbox].collidepoint(pos):
            if nextbox:
                lines.append((boxes[nextbox - 1].pos,boxes[nextbox].pos))
            nextbox += 1
        else:
            lines = []
            nextbox = 0
boxlines()
pgzrun.go()