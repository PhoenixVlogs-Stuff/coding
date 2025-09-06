import pgzrun
import random
WIDTH = 720
HEIGHT = 540
TITLE = "Coins & bombs - Version infdev"
bombs = ["bomb","nuke","tntbox","tnt"]
bombox = []
aaahhh = []
startspeed = 10
totalevel = 9
level = 1
die = False
win = False
def draw():
    global bombox
    screen.clear()
    screen.blit("field",(0,0))

    if die == False:
        screen.fill("#FF0000")
        screen.draw.text("You lose!",(0,0))
    elif win:
        screen.fill("#1AFF00")
        screen.draw.text("You won!",(0,0))
    else:
        for i in bombox:
            i.draw()
def update():
    global bombox
    if len(bombox) == 0:
        bombox = itemCreator(level)
def createOption(items2):
    global bombs
    createItems = ["coin"]
    for i in range(0,items2):
        gambling = random.choice(bombs)
        createItems.append(gambling)
    return createItems
def itemCreator(items2):
    createItems = createOption(items2)
    items = actorCreator(createItems)
    itemdisplay(items)
    itemAnimator(items)
    return items
def actorCreator(createItems):
    items = []
    for i in createItems:
        item = Actor(i)
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