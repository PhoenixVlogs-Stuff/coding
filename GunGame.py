import random
import pygame
import pgzrun
WIDTH = 720
HEIGHT = 540
TITLE = "Tenna shooting minigame - infdev"
T_rank = Actor("tenna")
message = ("")
score = 0
def draw():
    screen.fill("#000000")
    T_rank.draw()
    screen.draw.text(message,topleft = (300,0),fontsize = 50)
    screen.draw.text(str(score),topleft = (0,0),fontsize = 50)
def update():
    if keyboard.left:
        T_rank.x -= 10
    if keyboard.right:
        T_rank.x += 10
    if keyboard.up:
        T_rank.y -= 10
    if keyboard.down:
        T_rank.y += 10
def on_mouse_down(pos):
    global message
    global score
    if T_rank.collidepoint(pos):
        message = ("10 points!")
        T_rank.x = random.randint(0,660)
        T_rank.y = random.randint(0,460)
        score += 10
    else:
        message = ("You missed!")
        score -= 10
pgzrun.go()