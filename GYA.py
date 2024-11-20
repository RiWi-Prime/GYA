''' 
Game Title:     The Blorp Game  
About:          GYA - Funktions bas spel. Vilket betyder 
                att detta spel innehåller inte funktionerna.
Creators:       Rikard W, Sebastian B and Oscar K

Current Version: v.1.5.2
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
current_map = []

## CODE
game = True
print("The Blorp Game")
print("Verison V.1.5.2")

timer = 0
clock = 2
accel = 1
grav = 0

# IMAGES/ACTORS
blorp = Actor('blorp_grey.png',pos = (75,575))
blorp.image = 'blorp_grey.png'
pictures = ['empty.png','block_grey.png','block_pink.png','block_green.png','block_purple.png',
            'portal_pink.png','portal_green.png','portal_purple.png','portal_black.png',
            'block_dark_grey.png'
            ]

# WORLD DATA
base_map = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #25w, 13h 
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 5, 0, 0, 0, 6, 0, 0, 0, 7, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 9, 0, 0, 0, 9, 0, 0, 0, 9, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 9, 9, 9, 0, 9, 9, 9, 0, 9, 9, 9, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

map_a = [
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 8, 0, 2], 
[2, 0, 2, 2, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 2, 2, 0, 2], 
[2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 2, 2, 0, 0, 2, 0, 0, 2, 2, 0, 0, 2, 0, 0, 2], 
[2, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 0, 2, 2], 
[2, 0, 0, 0, 2, 0, 0, 2, 2, 0, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2], 
[2, 0, 2, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 2], 
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2], 
[2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
[2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
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
[3, 3, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 3, 0, 3, 0, 3, 3, 8, 3], 
[3, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 3, 0, 0, 0, 0, 3], 
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
[4, 0, 4, 0, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 0, 4], 
[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
]

current_map = base_map.copy()

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

def possible_move(deltax,deltay):
    global r
    blorp.x += deltax
    blorp.y += deltay
    for ri,row in enumerate(current_map):
        for ci,tile in enumerate(row):
                if tile and not tile in [5,6,7,8]:
                    # Smaller rect than tile 
                    r = Rect(ci*dx+5,ri*dy+5,dx-10,dy-10)
                    if blorp.colliderect(r):
                        #print(r,blorp.pos,tile)
                        blorp.x -= deltax
                        blorp.y -= deltay

                        return False
    blorp.x -= deltax
    blorp.y -= deltay
    r = None
    return True


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
    
    ### HOME 
    # HOME BASE TEXT
    if home == True:
        screen.draw.text('ENTER A PORTAL TO BEGIN!',(600,310),fontsize=55,color="darkgrey",alpha=0.4)

def update(dt):
    ### COLLIDERECT
    global map_level
    global clock
    global on_block
    ### NEXT LEVEL
    global map_level
    global current_map
    
    ## GOLDEN PORTAL
    # MAP A
    if map_level == 2:
        row = int((blorp.y +26) / tile_size)
        column = int(blorp.x / tile_size)
        tile = pictures[map_a[row][column]]
        if tile == "portal_black.png":
            map_level = 1
            blorp.pos = (75,575)
            current_map.clear()
            current_map = base_map.copy()
        if tile == "block_pink.png": #ADD BLOCK
            on_block = True
        else:
            on_block = False
    # MAP B
    if map_level == 3:
        row = int((blorp.y + 26) / tile_size)
        column = int(blorp.x / tile_size)
        tile = pictures[map_b[row][column]]
        if tile == "portal_black.png":
            map_level = 1
            blorp.pos = (75,575)
            current_map.clear()
            current_map = base_map.copy()
        if tile == "block_green.png": #ADD BLOCK
            on_block = True
        else:
            on_block = False
    # MAP C
    if map_level == 4:
        row = int((blorp.y +26) / tile_size)
        column = int(blorp.x / tile_size)
        tile = pictures[map_c[row][column]]
        if tile == "portal_black.png":
            map_level = 1
            blorp.pos = (75,575)
            current_map.clear()
            current_map = base_map.copy()
        if tile == "block_purple.png": #ADD BLOCK
            on_block = True
        else:
            on_block = False
            
    ## PORTALS BASE MAP / where you enter from 'HOME'
    if map_level == 1:
            row = int((blorp.y +26) / tile_size)
            column = int(blorp.x / tile_size)
            tile = pictures[base_map[row][column]]
            if tile == "portal_pink.png": #CHANGE PORTAL
                map_level = 2
                blorp.pos = (75,575)
                current_map.clear()
                current_map = map_a.copy()

            if tile == "portal_green.png": #CHANGE PORTAL
                map_level = 3
                blorp.pos = (75,575)
                current_map.clear()
                current_map = map_b.copy()

            if tile == "portal_purple.png": #CHANGE PORTAL
                map_level = 4
                blorp.pos = (75,575)
                current_map.clear()
                current_map = map_c.copy()

            if tile == "block_grey.png" or tile == "block_dark_grey.png": #ADD BLOCK
                on_block = True
            else:
                on_block = False
                
    ### MOVEMENT
    if keyboard.D and possible_move(3,0):
        blorp.x += 3

    if keyboard.A and possible_move(-3,0):
        blorp.x -= 3

    # BARRIER
    blorp.x = min(max(blorp.x,blorp.width//2),WIDTH-blorp.width//2)
    blorp.y = min(max(blorp.y,blorp.height//2),HEIGHT-blorp.height//2)

    # GRAVITATION
    clock += dt

    # JUMP
    if on_block == False and clock >= 0.4:
        if clock >= 0.45 and possible_move(0,1):
            blorp.y += 1
        if clock >= 0.6 and possible_move(0,2):
            blorp.y += 2
        if clock >= 0.8 and possible_move(0,2):
            blorp.y += 2
    if not blorp.y == min(max(blorp.y,blorp.height//2),HEIGHT-blorp.height//2):
        on_block = True        
    if (keyboard.space or keyboard.w) and on_block == True:
        clock = 0
        on_block = False
    if clock <= 0.4 and possible_move(0,-5.5):
        blorp.y -= 5.5
        if clock >= 0.2 and possible_move(0,1):
            blorp.y += 1
        if clock >= 0.3 and possible_move(0,1):
            blorp.y += 1
        if clock >= 0.35 and possible_move(0,2):
            blorp.y += 2


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