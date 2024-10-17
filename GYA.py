'''
    GYA - Funktions spel

Current Version v.12 
'''

## IMPORTS
import random
import pgzrun
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
blorp_purple = Actor('blorp_blue.png')

# OTHER-FUNKTIONS
#fine function
def other_funktions():
    pass

# FUNKTIONS
def draw():
    pass 

def update():
    pass

## END-CODE

#SCREEN
os.environ['SDL_VIDEO_CENTERED'] = '1'
pgzrun.go()

