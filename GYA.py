'''
    GYA - Funktions spel

Current Version v.12 
'''

## IMPORTS
import random
import pgzrun
import pygame
import os

HEIGHT = 650
WIDTH = 1280

## CODE
game = True
print("game")

# IMAGES/ACTORS
blorp_grey = Actor('blorp_grey.png')
existing = True
# OTHER-FUNKTIONS
'''Other funktions should placed here'''

# FUNKTIONS
def draw():
    ### BASIC DRAW (screen clear/blit/draw ect...)
    screen.clear()
    screen.blit('test_bg1.png',(0,0))
    blorp_grey.draw()



def update():
    ### MOVEMENT
    if keyboard.D:
        blorp_grey.x += 5
    if keyboard.A:
        blorp_grey.x -= 5
    if existing == True:
        blorp_grey.y += 5
    

    # BARRIER
    blorp_grey.x = min(max(blorp_grey.x,blorp_grey.width//2),WIDTH-blorp_grey.width//2)
    blorp_grey.y = min(max(blorp_grey.y,blorp_grey.height//2),HEIGHT-blorp_grey.height//2)

    # GRAVITATION
    

## END-CODE

#SCREEN
os.environ['SDL_VIDEO_CENTERED'] = '1'
pgzrun.go()

