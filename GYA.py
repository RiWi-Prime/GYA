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
timer = 0
clock = 2
accel = 1
grav = 1
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



def update(dt):
    ### MOVEMENT
    
    
    if keyboard.D:
        blorp_grey.x += 5

    if keyboard.A:
        blorp_grey.x -= 5
    
    

    # BARRIER
    blorp_grey.x = min(max(blorp_grey.x,blorp_grey.width//2),WIDTH-blorp_grey.width//2)
    blorp_grey.y = min(max(blorp_grey.y,blorp_grey.height//2),HEIGHT-blorp_grey.height//2)

    # GRAVITATION
    global timer

    if existing == True:
        global clock
        global accel
        global grav
        accel += dt
        clock += dt
        grav -= dt

        if  clock >= 2:
            blorp_grey.y += 2*accel

        if  not blorp_grey.y == min(max(blorp_grey.y,blorp_grey.height//2),HEIGHT-blorp_grey.height//2):
            accel = 1

        if keyboard.space:
            clock = 0
            grav = 1
        if clock <= 2:
            blorp_grey.y +=-5*grav
   

## END-CODE

#SCREEN
os.environ['SDL_VIDEO_CENTERED'] = '1'
pgzrun.go()

