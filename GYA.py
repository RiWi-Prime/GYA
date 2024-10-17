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
#blorp_main = actors('')
blorp_orange = Actor('blorp_orange.png')
blorp_red = Actor('blorp_red.png')
blorp_yellow = Actor('blorp_yellow.png')
blorp_blue = Actor('blorp_blue.png')
blorp_purple = Actor('blorp_purple.png')

# OTHER-FUNKTIONS
'''Other funktions should placed here'''

# FUNKTIONS
def draw():
    screen.clear()
    screen.blit('blorp_blue.png',(0,0))
    blorp_yellow.draw()

def update():
    ### MOVEMENT
    if keyboard.D:
        blorp_yellow.x += 5
    if keyboard.A:
        blorp_yellow.x -= 5

## END-CODE

#SCREEN
os.environ['SDL_VIDEO_CENTERED'] = '1'
pgzrun.go()

