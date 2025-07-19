import pygame
import pgzrun
WIDTH = 720
HEIGHT = 540
TITLE = "Tenna shooting minigame - infdev"
T_rank = Actor("tenna")
Z_rank = Actor("gunn")
Z_rank.pos = 560,375
def draw():
    screen.fill("#000000")
    T_rank.draw()
    Z_rank.draw()
pgzrun.go()