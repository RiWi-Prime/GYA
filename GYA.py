''' 
Game Title:     The Blorp Game   
About:          GYA - Funktions spel
Creators:       Rikard W, Sebastian B and Oscar K

Current Version: v.1.5.1
'''

## IMPORTS
import random
import pgzrun
import os

# Variables
HEIGHT = 650
WIDTH = 1250

Menu = False # KEYBOARD.I and X
Menu_value = 0 # KEYBOARD.I and X

home = False

existing = True
dx, dy = 50, 50

tile_size = 50

map_level = 1

## CODE
game = True
print("The Blorp Game")
print("Verison V.1.5.0")

timer = 0
clock = 2
accel = 1
grav = 0

# IMAGES/ACTORS
blorp = Actor('blorp_grey.png',pos = (75,575))
blorp.image = 'blorp_grey.png'
pictures = ['empty.png','block_grey.png','block_pink.png','block_green.png','block_purple.png',
            'portal_pink.png','portal_green.png','portal_purple.png','portal_black.png',
            'blorp_blue.png','blorp_light_blue.png','blorp_green.png','blorp_yellow.png',
            'blorp_red.png','blorp_magenta.png', 'block_dark_grey.png'
            ]

# WORLD DATA
base_map = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #25w, 13h 
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 5, 0, 0, 0, 6, 0, 0, 0, 7, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 15, 0, 0, 0, 15, 0, 0, 0, 15, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 15, 15, 15, 0, 15, 15, 15, 0, 15, 15, 15, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 6, 0, 0, 0, 7, 0, 0, 1], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

map_a = [
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 8, 0, 2], 
[2, 0, 2, 2, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 2, 0, 2, 2, 0, 0, 0, 2, 2, 0, 2], 
[2, 0, 0, 2, 2, 0, 0, 0, 2, 2, 0, 2, 2, 0, 2, 0, 0, 2, 2, 0, 0, 2, 0, 0, 2], 
[2, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 2, 2, 0, 0, 2, 2, 0, 0, 0, 2, 2], 
[2, 0, 0, 0, 2, 0, 0, 0, 2, 2, 0, 2, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2], 
[2, 0, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 2], 
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2], 
[2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
[2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 2], 
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
]

map_b = [
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
[3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 3, 3, 0, 0, 0, 3], 
[3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 3], 
[3, 3, 0, 3, 3, 3, 3, 3, 0, 3, 0, 3, 0, 3, 0, 3, 3, 3, 0, 3, 3, 3, 3, 0, 3], 
[3, 3, 0, 3, 0, 0, 3, 3, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3], 
[3, 3, 0, 3, 3, 0, 3, 0, 0, 3, 0, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 0, 3, 3], 
[3, 3, 0, 0, 3, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 3, 3, 0, 3, 3, 0, 0, 0, 0, 3], 
[3, 3, 3, 0, 3, 3, 0, 3, 3, 3, 3, 3, 0, 3, 0, 3, 3, 0, 0, 3, 0, 3, 3, 0, 3], 
[3, 3, 3, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 3, 3, 0, 3, 0, 3, 0, 0, 3], 
[3, 3, 0, 0, 0, 3, 3, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 3, 0, 3, 0, 3, 0, 3, 3], 
[3, 3, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 3, 0, 3, 0, 3, 3, 3, 3], 
[3, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 3, 0, 0, 0, 8, 3], 
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
]

map_c = [
[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
[4, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0, 8, 4], 
[4, 0, 4, 4, 4, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 4, 4, 0, 4, 0, 4, 4], 
[4, 0, 0, 4, 4, 0, 4, 0, 4, 4, 4, 0, 0, 0, 4, 0, 0, 4, 0, 0, 0, 4, 0, 0, 4], 
[4, 4, 0, 4, 4, 0, 0, 4, 0, 0, 0, 4, 0, 4, 0, 0, 4, 4, 0, 4, 4, 0, 4, 0, 4], 
[4, 0, 0, 4, 0, 4, 0, 0, 0, 4, 0, 0, 4, 4, 0, 4, 0, 4, 0, 0, 0, 4, 0, 0, 4], 
[4, 0, 4, 0, 0, 0, 4, 4, 4, 0, 4, 0, 4, 4, 0, 0, 4, 0, 4, 4, 0, 4, 0, 4, 4], 
[4, 0, 0, 4, 0, 4, 0, 0, 0, 4, 0, 0, 4, 0, 4, 0, 0, 4, 0, 0, 0, 4, 0, 0, 4], 
[4, 4, 0, 4, 4, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 4, 0, 4, 4, 0, 4, 0, 4], 
[4, 0, 0, 4, 0, 0, 4, 4, 4, 4, 4, 4, 4, 0, 4, 0, 0, 4, 0, 0, 0, 4, 0, 0, 4], 
[4, 0, 4, 4, 0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 4, 0, 4, 4, 0, 4, 0, 4, 4], 
[4, 0, 4, 0, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 8, 4], 
[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
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
    if map_level == 1:
        for row in range(len(base_map)):
            for column in range(len(base_map[row])):
                x = column * tile_size
                y = row * tile_size
                tile = pictures[base_map[row][column]]
                screen.blit(tile, (x, y))
                
    if map_level == 2:
        for row in range(len(map_a)):
            for column in range(len(map_a[row])):
                x = column * tile_size
                y = row * tile_size
                tile = pictures[map_a[row][column]]
                screen.blit(tile, (x, y))

    if map_level == 3:
        for row in range(len(map_b)):
            for column in range(len(map_b[row])):
                x = column * tile_size
                y = row * tile_size
                tile = pictures[map_b[row][column]]
                screen.blit(tile, (x, y))

    if map_level == 4:
        for row in range(len(map_c)):
            for column in range(len(map_c[row])):
                x = column * tile_size
                y = row * tile_size
                tile = pictures[map_c[row][column]]
                screen.blit(tile, (x, y))

def on_mouse_down(pos,button): 
     if button == mouse.RIGHT and blorp.collidepoint(pos):
          print('Du har inte råd/Köpet genomfördes') #Future shop funktion


# FUNKTIONS
def draw():
    ### BASIC DRAW (screen clear/blit/draw ect...)
    screen.clear()

    # MAP . DRAW
    if map_level == 1:
        screen.blit('background_grey',(0,0))
    if map_level == 2:
        screen.blit('background_pink',(0,0))
    if map_level == 3:
        screen.blit('background_green',(0,0))
    if map_level == 4:
        screen.blit('background_purple',(0,0))
        # ADD MORE UNDER

    #draw_grid()
    draw_tiles()
    
    blorp.draw()

    # MENU / COULD BE CONVERTED
    if Menu == True:
        screen.draw.text('MENU',(WIDTH/2, 100,),fontsize=50)
        screen.draw.text('CLOSE [X]',(WIDTH/1.2, 100,),fontsize=25)
    
    ### HOME 
    # HOME BASE TEXT
    if home == True:
        screen.draw.text('ENTER A PORTAL TO BEGIN!',(WIDTH/3,230),fontsize=65)


def update(dt):
    ### COLLIDERECT

    ### NEXT LEVEL
    global map_level

    ## GOLDEN PORTAL
    # MAP A
    if map_level == 2:
        row = int(blorp.y / tile_size)
        column = int(blorp.x / tile_size)
        tile = pictures[map_a[row][column]]
        if tile == "portal_black.png":
            map_level = 1
            # ADD POS HERE
    # MAP B
    if map_level == 3:
        row = int(blorp.y / tile_size)
        column = int(blorp.x / tile_size)
        tile = pictures[map_b[row][column]]
        if tile == "portal_black.png":
            map_level = 1
            # ADD POS HERE
    # MAP C
    if map_level == 4:
        row = int(blorp.y / tile_size)
        column = int(blorp.x / tile_size)
        tile = pictures[map_c[row][column]]
        if tile == "portal_black.png":
            map_level = 1
            # ADD POS HERE
            
    ## PORTALS BASE MAP / where you enter from 'HOME'
    if map_level == 1:
            row = int(blorp.y / tile_size)
            column = int(blorp.x / tile_size)
            tile = pictures[base_map[row][column]]
            if tile == "portal_pink.png": #CHANGE PORTAL
                map_level = 2
        
    if map_level == 1:
            row = int(blorp.y / tile_size)
            column = int(blorp.x / tile_size)
            tile = pictures[base_map[row][column]]
            if tile == "portal_green.png": #CHANGE PORTAL
                map_level = 3

    if map_level == 1:
            row = int(blorp.y / tile_size)
            column = int(blorp.x / tile_size)
            tile = pictures[base_map[row][column]]
            if tile == "portal_purple.png": #CHANGE PORTAL
                map_level = 4

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
        
        # JUMP
        if (keyboard.space or keyboard.w) and accel == 1:
            clock = 0
            grav = 1
        if not accel == 1:
            blorp.y +=-5*grav

            # Makes you jump slower / can also be adjusted to jump faster
            if keyboard.A:
                blorp.x += 0.25
            if keyboard.D:
                blorp.x -= 0.25
            # ------------------

            blorp.image = 'blorp_grey_jump.png'


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
    
    ### HOME
    global home
    if map_level == 1:
        home = True
    else:
        home = False


## END-CODE

#SCREEN
os.environ['SDL_VIDEO_CENTERED'] = '1'
pgzrun.go()