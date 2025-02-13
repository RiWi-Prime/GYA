'''
    GYA - Funktions spel
Current Version v.12 
'''
## IMPORTS
import random
import pgzrun
import os
#Variables
HEIGHT = 650
WIDTH = 1280
tile_size = 50
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
def draw_grid():
	for line in range(0, 30):
		screen.draw.line((0, line * tile_size), (WIDTH, line * tile_size), (255, 255, 255))
		screen.draw.line((line * tile_size, 0), (line * tile_size, HEIGHT), (255, 255, 255))
# FUNKTIONS
def draw():
    ### BASIC DRAW (screen clear/blit/draw ect...)
    screen.clear()
    screen.blit('test_bg1.png',(0,0))
    blorp_grey.draw()
    draw_grid()
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
            if (keyboard.space or keyboard.w) and accel == 1:
                clock = 0
                grav = 1
            if clock <= 2:
                if clock <= 2 or not accel == 1:
                    blorp_grey.y +=-5*grav


## END-CODE
#SCREEN
os.environ['SDL_VIDEO_CENTERED'] = '1'
pgzrun.go()