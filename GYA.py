'''
    GYA - Funktions spel

Current Version v.12 
'''

## IMPORTS
import random
import pgzrun
import pygame
import os

## CODE
game = True
print("game")

# IMAGES/ACTORS
blorp_grey = Actor('blorp_grey.png')


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
    
    # GRAVITATION
    

## END-CODE

#SCREEN
os.environ['SDL_VIDEO_CENTERED'] = '1'
pgzrun.go()

