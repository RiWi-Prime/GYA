'''
    GYA - Funktions spel

Current Version v.13 
'''

## IMPORTS
import random
import pgzrun
import os

#Variables
HEIGHT = 650
WIDTH = 1250
tile_size = 50
Menu = False # KEYBOARD.I
Menu_value = 0 # KEYBOARD.I
existing = True

## CODE
game = True
print("game")
timer = 0
clock = 2
accel = 1
grav = 0

# IMAGES/ACTORS
blorp = Actor('blorp_grey.png',pos = (100,100))
blorp.image = 'blorp_grey.png'

# OTHER-FUNKTIONS
def draw_grid():
	for line in range(0, 30):
		screen.draw.line((0, line * tile_size), (WIDTH, line * tile_size), (255, 255, 255))
		screen.draw.line((line * tile_size, 0), (line * tile_size, HEIGHT), (255, 255, 255))

def on_mouse_down(pos,button): 
     if button == mouse.RIGHT and blorp_grey.collidepoint(pos):
          print('Du har inte råd/Köpet genomfördes') #Future shop funktion

# FUNKTIONS
def draw():
    ### BASIC DRAW (screen clear/blit/draw ect...)
    screen.clear()
    screen.blit('test_bg1.png',(0,0))
    blorp.draw()
    draw_grid()

    # MENU BUTTEN / COULD BE CONVERTED
    if Menu == True:
        screen.draw.text('MENU',(WIDTH/2, 100,),fontsize=50)
        screen.draw.text('CLOSE [X]',(WIDTH/1.2, 100,),fontsize=25)



def update(dt):
    ### MOVEMENT
    if keyboard.D:
        blorp.x += 3

    if keyboard.A:
        blorp.x -= 3

    # BARRIER
    blorp.x = min(max(blorp.x,blorp.width//2),WIDTH-blorp.width//2)
    blorp.y = min(max(blorp.y,blorp.height//2),HEIGHT-blorp.height//2)

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
            blorp.y += 2*accel

        if  not blorp.y == min(max(blorp.y,blorp.height//2),HEIGHT-blorp.height//2):
            accel = 1
            blorp.image = 'blorp_grey.png'

    ## KEYSBOARD BUTTONS
    # JUMP
        if (keyboard.space or keyboard.w) and accel == 1:
            clock = 0
            grav = 1
        if not accel == 1:
            blorp.y +=-5*grav
            blorp.image = 'blorp_blue.png'
   

    ## KEYSBOARD BUTTONS
    # MENU
    '''Create a variable that contains a number, so that when pressing
       [I] the menu will not close instantly when you let go of the key.
       
       You will have to press it again!

       Menu_value have the values 0, 1 or 2
       Menu is True or False'''
    global Menu
    global Menu_value
    if Menu_value == 1:
        Menu = True
    if Menu_value >= 2:
        Menu = False
        Menu_value = 0

    if keyboard.I: 
        Menu_value = 1
    if keyboard.X:
        Menu_value = 2


## END-CODE

#SCREEN
os.environ['SDL_VIDEO_CENTERED'] = '1'
pgzrun.go()