''' 
Game Title:     The Blorp Game   
About:          GYA - Funktions spel
Creators:       Rikard W, Sebastian B and Oscar K

Current Version: v.14
'''

## IMPORTS
import random
import pgzrun
import os

#Variables
HEIGHT = 650
WIDTH = 1250

Menu = False # KEYBOARD.I and X
Menu_value = 0 # KEYBOARD.I and X

existing = True
dx, dy = 50, 50

tile_size = 50

map_level = 1

## CODE
game = True
print("The Blorp Game")

timer = 0
clock = 2
accel = 1
grav = 0

# IMAGES/ACTORS
blorp = Actor('blorp_grey.png',pos = (100,100))
blorp.image = 'blorp_grey.png'
pictures = ['test_bg5','test_bg4','test_bg6']

# WORLD DATA
base_map = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #25w, 13h 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# OTHER-FUNKTIONS
def draw_grid():
    '''draw a nXn grid'''
    x,y = 0,0

    for _ in range(tile_size+1):
        screen.draw.line((x,0),(x,HEIGHT),'red')
        screen.draw.line((0,y),(WIDTH,y),'red')
        x += dx 
        y += dy 

def draw_tiles():
    for row in range(len(base_map)):
        for column in range(len(base_map[row])):
            x = column * tile_size
            y = row * tile_size
            tile = pictures[base_map[row][column]]
            screen.blit(tile, (x, y))

def on_mouse_down(pos,button): 
     if button == mouse.RIGHT and blorp.collidepoint(pos):
          print('Du har inte råd/Köpet genomfördes') #Future shop funktion


# FUNKTIONS
def draw():
    ### BASIC DRAW (screen clear/blit/draw ect...)
    screen.clear()
    screen.blit('test_bg1.png',(0,0))
    draw_grid()
    if map_level == 1:
        draw_tiles()
    blorp.draw()

    # DRAW OBSTICALS


    # MENU BUTTEN / COULD BE CONVERTED
    if Menu == True:
        screen.draw.text('MENU',(WIDTH/2, 100,),fontsize=50)
        screen.draw.text('CLOSE [X]',(WIDTH/1.2, 100,),fontsize=25)


def update(dt):
    ### COLLIDERECT
    
    ### NEXT LEVEL

    ### MOVEMENT
    if keyboard.D:
        blorp.x += 3
        blorp.image = 'blorp_red.png'

    if keyboard.A:
        blorp.x -= 3
        blorp.image = 'blorp_red.png'

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
            if keyboard.A or keyboard.D:
                blorp.image = 'blorp_red.png'
        
        
    ## KEYSBOARD BUTTONS
    # JUMP
        if (keyboard.space or keyboard.w) and accel == 1:
            clock = 0
            grav = 1
        if not accel == 1:
            blorp.y +=-5*grav
            blorp.image = 'blorp_blue.png'
            if keyboard.A or keyboard.D:
                blorp.image = 'blorp_red.png'


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