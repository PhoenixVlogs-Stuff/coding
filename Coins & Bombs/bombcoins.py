import pgzrun
import random
WIDTH = 720
HEIGHT = 540
TITLE = "Coins & bombs - Version infdev"
bombs = ["Bomb","nuke","nuke","TNT box","TNT"]
bombox = []
aaahhh = []
startspeed = 10
totalevel = 10
level = 1
die = False
win = False
def draw():
    global bombox
    screen.clear()
    screen.blit("field",(0,0))
    for i in bombox:
        i.draw()

def createOption(items2):
    global bombs
    createItems = ["coin"]
    for i in range(0,items2):
        gambling = random.choice(bombs)
        createItems.append(gambling)
    return createItems
def itemCreator(items2):
    CreateItems = createOption(items2)
    items = actorCreator(CreateItems)
    itemdisplay(items)
    itemAnimator(items)
    return items
def actorCreator(CreateItems):
    items = []
    for i in CreateItems:
        item = Actor(i+"img")
        items.append(item)
    return items
def itemdisplay(di):
    gaps = len(di)+1
    gapsize = WIDTH/gaps
    random.shuffle(di)
    for i,j in enumerate(di):
        newx = (i+1) * gapsize
        j.x = newx
def itemAnimator(ati):
    global aaahhh, startspeed, level
    for i in ati:
        duration = startspeed - level
        i.anchor = ("center", "bottom")
        animation = animate(i,duration = duration, on_finished = gameover(),y = HEIGHT)
        aaahhh.append(animation)
def gameover():
    global die
    die = True
def gamecomplete():
    global level, bombox, aaahhh, win
    stopanimation(aaahhh)
    if level == totalevel:
        win = True
    else:
        level += 1
        bombox = []
        aaahhh = []
def on_mouse_down(pos):
    global bombox, level
    for i in bombox:
        if i.collidepoint(pos):
            if "coin" in i.image:
                gamecomplete()
            else:
                gameover()
def stopanimation(stopanim):
    for i in stopanim:
        if i.running:
            i.stop()
pgzrun.go()