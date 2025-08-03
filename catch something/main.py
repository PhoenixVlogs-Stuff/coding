import pgzrun
TITLE = "Coin grabbing minigame - (Version infdev)"
WIDTH = 720
HEIGHT = 540
kris_where_the_hell_are_we = Actor("kris")
coin = Actor("coin")
def draw():
    screen.fill("#FFFFFF")
    kris_where_the_hell_are_we.draw()
    coin.draw()
DS = 0
def update():
    global DS
    if keyboard.left:
        kris_where_the_hell_are_we.x -= 7.5
    if keyboard.right:
        kris_where_the_hell_are_we.x += 7.5
    if keyboard.up:
        kris_where_the_hell_are_we.y -= 7.5
    if keyboard.down:
        kris_where_the_hell_are_we.y += 7.5
    touch =  kris_where_the_hell_are_we.colliderect(coin)
    if touch:
        DS = DS + 10
    print(DS)
pgzrun.go()