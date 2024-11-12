''' 
Game Title:     The Blorp Game   
About:          GYA - Funktions spel
Creators:       Rikard W, Sebastian B and Oscar K

Current Version: v.1.5.3
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

money = 100000

loot = ["blorp_special.png"]
spin_the_wheel = 0
# unlock color
unlock_blue = False
unlock_light_blue = False
unlock_green = False
unlock_yellow = False
unlock_red = False
unlock_megenta= False
# unlock special and ultimate
unlock_special = False
unlock_ultimate = False


## CODE
game = True
print("The Blorp Game")
print("Verison V.1.5.3")

timer = 0
clock = 2
on_block = True

# IMAGES/ACTORS
blorp_select = 'blorp_grey.png'
blorp = Actor(f'{blorp_select}',pos = (75,575))
#blorp.image = 'blorp_grey.png'
blorp_color = 1
casino = Actor('sign_casino.png',pos = (225,125))
sign = Actor('sign_wood.png',pos = (875,75))
wheel = Actor('casino_wheel.png',pos = (225,250))
pictures = ['empty.png','block_grey.png','block_pink.png','block_green.png','block_purple.png',
            'portal_pink.png','portal_green.png','portal_purple.png','portal_black.png',
            'blorp_blue.png','blorp_light_blue.png','blorp_green.png','blorp_yellow.png',
            'blorp_red.png','blorp_magenta.png', 'block_dark_grey.png','block_red.png'
            ]

# WORLD DATA
base_map = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #25w, 13h 
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 16, 16, 16, 16, 16, 16, 16, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
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
[2, 0, 2, 2, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 2, 2, 0, 2], 
[2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 2, 2, 0, 0, 2, 0, 0, 2, 2, 0, 0, 2, 0, 0, 2], 
[2, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 0, 2, 2], 
[2, 0, 0, 0, 2, 0, 0, 2, 2, 0, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2], 
[2, 0, 2, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 2], 
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
     global money
     if button == mouse.LEFT and blorp.collidepoint(pos):
        if money >= 50:
            loot_box()
            money -= 50
        else:
            print('You need more money!')

def loot_box():
    global unlock_special
    global unlock_ultimate
    spin_the_wheel = random.randint(0,1000)
    if spin_the_wheel == 1000:
        print('You won "GLITCHED BLORP"')
        unlock_special = True
    else:
        print(f'Your number was {spin_the_wheel}, You lost!')
    if spin_the_wheel in [100,110,120,130,140,150,160,170,180,190,200]:
        print('You won "ULTIMATE BLORP"')
        unlock_ultimate = True

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
        screen.draw.text('ENTER A PORTAL TO BEGIN!',(600,310),fontsize=55,color="darkgrey",alpha=0.4)
        screen.draw.text(f'Money : {money} B',(10,10),fontsize=25,color="gold")
        casino.draw()
        sign.draw()
        wheel.draw()
        screen.draw.text('COSMETICS',(760,60),fontsize=55,color='black',alpha=0.6)

        ## UNLOCK GUI
        # BLUE
        if unlock_blue != False:
            screen.draw.text('Owned',(600,125),fontsize=25,color='silver',alpha=1)
        else:
            screen.draw.text('25 B',(610,125),fontsize=25,color='gold',alpha=1)
        # LIGHT BLUE
        if unlock_light_blue != False:
            screen.draw.text('Owned',(700,125),fontsize=25,color='silver',alpha=1)
        else:
            screen.draw.text('25 B',(710,125),fontsize=25,color='gold',alpha=1)
        # GREEN
        if unlock_green != False:
            screen.draw.text('Owned',(800,125),fontsize=25,color='silver',alpha=1)
        else:
            screen.draw.text('25 B',(810,125),fontsize=25,color='gold',alpha=1)
        # YELLOW
        if unlock_yellow != False:
            screen.draw.text('Owned',(900,125),fontsize=25,color='silver',alpha=1)
        else:
            screen.draw.text('25 B',(910,125),fontsize=25,color='gold',alpha=1)
        # RED
        if unlock_red != False:
            screen.draw.text('Owned',(1000,125),fontsize=25,color='silver',alpha=1)
        else:
            screen.draw.text('25 B',(1010,125),fontsize=25,color='gold',alpha=1)
        # MEGENTA
        if unlock_megenta != False:
            screen.draw.text('Owned',(1100,125),fontsize=25,color='silver',alpha=1)
        else:
            screen.draw.text('25 B',(1110,125),fontsize=25,color='gold',alpha=1)

def update(dt):
    ### COLLIDERECT

    ### NEXT LEVEL
    global map_level
    global money
    global clock
    global on_block
    ## GOLDEN PORTAL
    # MAP A
    if map_level == 2:
        row = int((blorp.y + 26)/ tile_size)
        column = int(blorp.x / tile_size)
        tile = pictures[map_a[row][column]]
        if tile == "portal_black.png":
            map_level = 1
            money += 10 # change value
            blorp.pos = (75,575)
        if tile == "block_pink.png" or tile == "block_dark_grey.png": #ADD BLOCK
            on_block = True
        else:
            on_block = False

    # MAP B
    if map_level == 3:
        row = int((blorp.y + 26)/ tile_size)
        column = int(blorp.x / tile_size)
        tile = pictures[map_b[row][column]]
        if tile == "portal_black.png":
            map_level = 1
            money += 25 # change value 
            blorp.pos = (75,575)
        if tile == "block_green.png" or tile == "block_dark_grey.png": #ADD BLOCK
            on_block = True
        else:
            on_block = False    
    # MAP C
    if map_level == 4:
        row = int((blorp.y + 26) / tile_size)
        column = int(blorp.x / tile_size)
        tile = pictures[map_c[row][column]]
        if tile == "portal_black.png":
            map_level = 1
            money += 50 # change value
            blorp.pos = (75,575)
        if tile == "block_purple.png" or tile == "block_dark_grey.png": #ADD BLOCK
            on_block = True
        else:
            on_block = False    
            
    ## PORTALS BASE MAP / where you enter from 'HOME'
    if map_level == 1:
            row = int((blorp.y + 26) / tile_size)
            column = int(blorp.x / tile_size)
            tile = pictures[base_map[row][column]]
            if tile == "portal_pink.png": #CHANGE PORTAL
                map_level = 2
                blorp.pos = (75,575)

            if tile == "portal_green.png": #CHANGE PORTAL
                map_level = 3
                blorp.pos = (75,575)

            if tile == "portal_purple.png": #CHANGE PORTAL
                map_level = 4
                blorp.pos = (75,575)
            
            if tile == "block_grey.png" or tile == "block_dark_grey.png" or tile == "block_red.png": #ADD BLOCK
                on_block = True
            else:
                on_block = False

            ## BUY SKINS
            global blorp_select
            global blorp_color
            global unlock_blue
            global unlock_light_blue
            global unlock_green
            global unlock_yellow
            global unlock_red
            global unlock_megenta
            global unlock_special
            global unlock_ultimate
            # BLUE
            if not blorp_color == 2 and money >= 25:
                if tile == "blorp_blue.png":
                    blorp_color = 2
                    blorp_select = 'blorp_blue.png'
                    if unlock_blue != True:
                        money -= 25
                        unlock_blue = True
            # LIGHT BLUE
            if not blorp_color == 3 and money >= 25:
                if tile == "blorp_light_blue.png":
                    blorp_color = 3
                    blorp_select = 'blorp_light_blue.png'
                    if unlock_light_blue != True:
                        money -= 25
                        unlock_light_blue = True
            # GREEN
            if not blorp_color == 4 and money >= 25:
                if tile == "blorp_green.png":
                    blorp_color = 4
                    blorp_select = 'blorp_green.png'
                    if unlock_green != True:
                        money -= 25
                        unlock_green = True
            # YELLOW
            if not blorp_color == 5 and money >= 25:
                if tile == "blorp_yellow.png":
                    blorp_color = 5
                    blorp_select = 'blorp_yellow.png'
                    if unlock_yellow != True:
                        money -= 25
                        unlock_yellow = True
            # RED
            if not blorp_color == 6 and money >= 25:
                if tile == "blorp_red.png":
                    blorp_color = 6
                    blorp_select = 'blorp_red.png'
                    if unlock_red != True:
                        money -= 25
                        unlock_red = True
            # MAGENTA
            if not blorp_color == 7 and money >= 25:
                if tile == "blorp_magenta.png":
                    blorp_color = 7
                    blorp_select = 'blorp_magenta.png'
                    if unlock_megenta != True:
                        money -= 25
                        unlock_megenta = True
            # SPEICAL
            if unlock_special == True:
                blorp_color = 1000
                blorp_select = 'blorp_special.png'
            # ULTIMATE
            # ADD HERE

    ### MOVEMENT
    if keyboard.D:
        blorp.x += 3

    if keyboard.A:
        blorp.x -= 3

    # BARRIER
    blorp.x = min(max(blorp.x,blorp.width//2),WIDTH-blorp.width//2)
    blorp.y = min(max(blorp.y,blorp.height//2),HEIGHT-blorp.height//2)

    # GRAVITATION
    clock += dt
  
    # JUMP
    if on_block == False and clock >= 0.4:
        if clock >= 0.45:
            blorp.y += 1
        if clock >= 0.6:
            blorp.y += 2
        if clock >= 0.8:
            blorp.y += 2
    if not blorp.y == min(max(blorp.y,blorp.height//2),HEIGHT-blorp.height//2):
        on_block = True        
    if (keyboard.space or keyboard.w) and on_block == True:
        clock = 0
        on_block = False
    if clock <= 0.4:
        blorp.y -= 5.5
        if clock >= 0.2:
            blorp.y += 1
        if clock >= 0.3:
            blorp.y += 1
        if clock >= 0.35:
            blorp.y += 2
    if on_block == True:
            blorp.image = blorp_select

            # Makes you jump slower / can also be adjusted to jump faster
            if keyboard.A:
                blorp.x += 0.25
            if keyboard.D:
                blorp.x -= 0.25
            # ------------------

    # While jumping
    if on_block == False:
            if blorp_color == 1:
                blorp.image = 'blorp_grey_jump.png'
            if blorp_color == 2:
                blorp.image = 'blorp_blue_jump.png'
            if blorp_color == 3:
                blorp.image = 'blorp_light_blue_jump.png'
            if blorp_color == 4:
                blorp.image = 'blorp_green_jump.png'
            if blorp_color == 5:
                blorp.image = 'blorp_yellow_jump.png'
            if blorp_color == 6:
                blorp.image = 'blorp_red_jump.png'
            if blorp_color == 7:
                blorp.image = 'blorp_magenda_jump.png'
            if blorp_color == 1000:
                blorp.image = 'blorp_special.png' # CHANGE HERE TO JUMP
                


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

    ### LOOT BOXES
    global loot
    global spin_the_wheel


## END-CODE

#SCREEN
os.environ['SDL_VIDEO_CENTERED'] = '1'

pgzrun.go()