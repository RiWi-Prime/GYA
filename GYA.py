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

# IMAGES/ACTORS
blorp_grey = Actor('blorp_grey.png')
existing = True
# OTHER-FUNKTIONS
'''Other funktions should placed here'''

def draw_grid():
	for line in range(0, 20):
		pygame.draw.line(pygame.surface, (255, 255, 255), (0, line * tile_size), (WIDTH, line * tile_size))
		pygame.draw.line(pygame.surface, (255, 255, 255), (line * tile_size, 0), (line * tile_size, HEIGHT))

# FUNKTIONS
def draw():
    ### BASIC DRAW (screen clear/blit/draw ect...)
    screen.clear()
    screen.blit('test_bg1.png',(0,0))
    blorp_grey.draw()
    draw_grid()



def update():
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
    timer += 0.1
    if existing == True:
        blorp_grey.y += 2*timer

## END-CODE

#SCREEN
os.environ['SDL_VIDEO_CENTERED'] = '1'
pgzrun.go()

