''' 
Game Title:     The Blorp Game   
About:          GYA - Funktions spel
Creators:       Rikard W, Sebastian B and Oscar K

Current Version: v.2.0.0 
'''

## IMPORTS
import random
import pgzrun
import os

# Variables
HEIGHT = 650
WIDTH = 1250

difficulty = False

Menu = False # KEYBOARD.I and X
Menu_value = 0 # KEYBOARD.I and X

home = False

existing = True
dx, dy = 50, 50

tile_size = 50

map_level = 1
current_map = []
timer = 0
gliched_blorp = False
ultimate_blorp = False
nothing = False
got_money = False
money = 0
gambling = True



loot = ["blorp_special.png","blorp_ulimate.png"]
spin_the_wheel = 0
price_1 = False
price_2 = False
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
print("Verison V.2.0.0")

timer = 0
clock = 2
on_block = True

### IMAGES/ACTORS
blorp_select = 'blorp_grey.png'
blorp = Actor(f'{blorp_select}',pos = (75,575))
#blorp.image = 'blorp_grey.png'
blorp_color = 1
# Yes and No + blorp preview
blorp_preview_1 = Actor('blorp_glitch',pos=(325,270)) #230, 200
blorp_preview_2 = Actor('blorp_ultimate',pos=(325,385))
yes_button = Actor('yes.png',pos=(290, 335))
no_button = Actor('no.png',pos=(360, 335))
yes_button_2 = Actor('yes.png',pos=(290,450))
no_button_2 = Actor('no.png',pos=(360,450))
# Switches
switch_easy = Actor('switch_normal.png',pos=(950,450))
switch_hard = Actor('switch_difficult.png',pos=(950,450))
# Lock
lock = Actor('lock.png',pos=(290,300))
lock2 = Actor('lock.png',pos=(290,425))
# Other
casino_display = Actor('casino_display.png',pos = (175,375))
casino = Actor('sign_casino.png',pos = (300,100))
sign = Actor('sign_wood.png',pos = (875,75))
wheel = Actor('casino_wheel.png',pos = (175,200))
menu_background = Actor('menu.png',pos = (650,300))
pictures = ['empty.png','block_grey.png','block_pink.png','block_green.png','block_purple.png',
            'portal_pink.png','portal_green.png','portal_purple.png','portal_black.png',
            'blorp_blue.png','blorp_light_blue.png','blorp_green.png','blorp_yellow.png',
            'blorp_red.png','blorp_magenta.png', 'block_dark_grey.png','block_red.png', 'block_void.png'
            ]
backgrounds = ['background_grey.png','background_pink.png','background_green.png','background_purple.png',
               'background_pink.png','background_green.png','background_purple.png']

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
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

map_a = [
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2], 
[2, 0, 0, 2, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 2, 0, 0, 2, 0, 0, 0, 2, 2, 0, 2], 
[2, 0, 2, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2], 
[2, 0, 0, 2, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 2], 
[2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 2], 
[2, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 2], 
[2, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2], 
[2, 8, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
[2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 2, 2], 
[2, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2], 
[2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
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

map_da = [
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 2, 0, 0, 0, 0, 17, 2, 2, 8, 0, 2], 
[2, 0, 2, 2, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 2, 2, 0, 2], 
[2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 2, 2, 0, 0, 2, 0, 0, 17, 2, 0, 0, 2, 0, 0, 17], 
[2, 2, 0, 2, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0, 2, 2, 0, 0, 17, 2, 0, 0, 0, 2, 2], 
[2, 17, 0, 0, 2, 0, 0, 2, 2, 0, 2, 2, 17, 0, 2, 0, 0, 0, 0, 17, 0, 0, 2, 2, 2], 
[2, 0, 2, 0, 0, 17, 17, 0, 2, 2, 2, 0, 0, 0, 0, 0, 2, 17, 0, 17, 0, 0, 0, 2, 2], 
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 0, 0, 0, 17, 0, 0, 0, 17, 2, 0, 0, 2], 
[2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 17, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
[2, 17, 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
[2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
[2, 2, 2, 2, 2, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17],
]

map_db = [
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
[3, 3, 3, 3, 3, 3, 3, 17, 0, 0, 0, 3, 3, 3, 3, 17, 0, 0, 0, 3, 3, 0, 0, 0, 17], 
[3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 3], 
[3, 3, 0, 3, 3, 3, 3, 3, 0, 3, 0, 3, 0, 3, 0, 3, 3, 3, 0, 3, 3, 3, 17, 0, 3], 
[3, 3, 0, 3, 17, 0, 3, 3, 0, 3, 0, 0, 0, 17, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3], 
[3, 3, 0, 3, 3, 0, 3, 0, 0, 3, 0, 3, 3, 3, 3, 3, 3, 0, 17, 3, 3, 17, 0, 3, 3], 
[3, 3, 0, 0, 3, 0, 0, 0, 3, 17, 0, 0, 0, 0, 0, 3, 3, 0, 3, 17, 0, 0, 0, 0, 3], 
[3, 3, 17, 0, 3, 3, 0, 3, 3, 3, 3, 3, 0, 3, 0, 3, 3, 0, 0, 3, 0, 3, 3, 0, 3], 
[3, 3, 3, 0, 17, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 17, 3, 3, 0, 3, 0, 3, 0, 0, 3], 
[3, 3, 0, 0, 0, 17, 3, 0, 3, 3, 3, 3, 3, 17, 0, 0, 0, 3, 0, 3, 0, 3, 0, 17, 3], 
[3, 3, 0, 3, 0, 0, 0, 0, 0, 0, 17, 0, 0, 0, 0, 3, 0, 3, 0, 3, 0, 3, 3, 8, 3], 
[3, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 3, 0, 0, 0, 0, 3], 
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
]

map_dc = [
[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
[4, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0, 8, 4], 
[4, 0, 4, 4, 4, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 4, 4, 0, 17, 0, 4, 4], 
[17, 0, 0, 4, 4, 0, 17, 0, 4, 4, 4, 0, 0, 0, 4, 0, 0, 4, 0, 0, 0, 17, 0, 0, 17], 
[4, 4, 0, 4, 17, 0, 0, 17, 0, 0, 0, 4, 0, 4, 0, 0, 4, 17, 0, 4, 4, 0, 4, 0, 4], 
[4, 0, 0, 17, 0, 4, 0, 0, 0, 4, 0, 0, 4, 4, 0, 4, 0, 17, 0, 0, 0, 4, 0, 0, 4], 
[4, 0, 4, 0, 0, 0, 4, 4, 4, 0, 4, 0, 17, 17, 0, 0, 4, 0, 4, 4, 0, 17, 0, 4, 4], 
[17, 0, 0, 4, 0, 17, 0, 0, 0, 17, 0, 0, 17, 0, 4, 0, 0, 4, 0, 0, 0, 17, 0, 0, 17], 
[4, 4, 0, 4, 17, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 17, 0, 4, 4, 0, 4, 0, 4], 
[4, 0, 0, 17, 0, 0, 4, 17, 4, 4, 4, 17, 4, 0, 4, 0, 0, 17, 0, 0, 0, 4, 0, 0, 4], 
[4, 0, 4, 4, 0, 4, 0, 0, 0, 17, 0, 0, 0, 4, 0, 0, 4, 0, 4, 4, 0, 17, 0, 4, 4], 
[4, 0, 4, 17, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 17, 0, 0, 0, 0, 4], 
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
    
    if map_level == 5:
        for row in range(len(map_da)):
            for column in range(len(map_da[row])):
                x = column * tile_size
                y = row * tile_size
                tile = pictures[map_da[row][column]]
                screen.blit(tile, (x, y))
    
    if map_level == 6:
        for row in range(len(map_db)):
            for column in range(len(map_db[row])):
                x = column * tile_size
                y = row * tile_size
                tile = pictures[map_db[row][column]]
                screen.blit(tile, (x, y))
    
    if map_level == 7:
        for row in range(len(map_dc)):
            for column in range(len(map_dc[row])):
                x = column * tile_size
                y = row * tile_size
                tile = pictures[map_dc[row][column]]
                screen.blit(tile, (x, y))

def possible_move(deltax,deltay):
    global r
    blorp.x += deltax
    blorp.y += deltay
    for ri,row in enumerate(current_map):
        for ci,tile in enumerate(row):
                if tile and not tile in [5,6,7,8,9,10,11,12,13,14]:
                    # Smaller rect than tile 
                    r = Rect(ci*dx+5,ri*dy+5,dx-10,dy-10)
                    if blorp.colliderect(r):
                        #print(r,blorp.pos,tile)
                        blorp.x -= deltax
                        blorp.y -= deltay
                        if tile == 17:
                            blorp.x = 75
                            blorp.y = 575

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
    screen.blit(backgrounds[map_level-1],(0,0))

    draw_tiles()
    
    ### HOME 
    # HOME BASE TEXT
    if home == True:
        screen.draw.text('ENTER A PORTAL TO BEGIN!',(600,310),fontsize=55,color="darkgrey",alpha=0.4)
        screen.draw.text(f'Money : {money} B',(10,10),fontsize=25,color="gold")
        wheel.draw()
        casino.draw()
        sign.draw()
        screen.draw.text('COSMETICS',(760,60),fontsize=55,color='black',alpha=0.6)
        screen.draw.text('Press [i] to open the Menu',(100,610),fontsize=25,color='darkgrey',alpha=0.7)
        screen.draw.text(f'50 B',(160,75),fontsize=25,color="gold")

        ## UNLOCK GUI
        # BLUE
        if unlock_blue != False:
            screen.draw.text('Owned',(600,125),fontsize=25,color='silver',alpha=1)
        else:
            screen.draw.text('50 B',(610,125),fontsize=25,color='gold',alpha=1)
        # LIGHT BLUE
        if unlock_light_blue != False:
            screen.draw.text('Owned',(700,125),fontsize=25,color='silver',alpha=1)
        else:
            screen.draw.text('50 B',(710,125),fontsize=25,color='gold',alpha=1)
        # GREEN
        if unlock_green != False:
            screen.draw.text('Owned',(800,125),fontsize=25,color='silver',alpha=1)
        else:
            screen.draw.text('50 B',(810,125),fontsize=25,color='gold',alpha=1)
        # YELLOW
        if unlock_yellow != False:
            screen.draw.text('Owned',(900,125),fontsize=25,color='silver',alpha=1)
        else:
            screen.draw.text('50 B',(910,125),fontsize=25,color='gold',alpha=1)
        # RED
        if unlock_red != False:
            screen.draw.text('Owned',(1000,125),fontsize=25,color='silver',alpha=1)
        else:
            screen.draw.text('50 B',(1010,125),fontsize=25,color='gold',alpha=1)
        # MEGENTA
        if unlock_megenta != False:
            screen.draw.text('Owned',(1100,125),fontsize=25,color='silver',alpha=1)
        else:
            screen.draw.text('50 B',(1110,125),fontsize=25,color='gold',alpha=1)
        
                            #screen.draw.text(f' {timer:.1f}',centerx=WIDTH/2,centery=100,fontsize=60,color='black')
        
        ## CASINO DISPLAY
        casino_display.draw()
        if gliched_blorp == False and ultimate_blorp == False and nothing == False and got_money == False:
            screen.draw.text('Press the wheel to spin!',(98,370),fontsize=20,color='orange',alpha = (0.9))

        #(175,375)
        # SCREEN OF DISPLAY
        if gliched_blorp == True:
            screen.draw.text(f'You won "GLITCHED BLORP"',(96,368),fontsize=17,color='purple',alpha = (0.9))
            # Fix posistion when display is added
        if ultimate_blorp == True:
            screen.draw.text(f'You won "ULTIMATE BLORP"',(96,368),fontsize=17,color='pink',alpha = (0.9))
            # Fix posistion when display is added
        if nothing == True:
            screen.draw.text(f'You lost',(125,363),fontsize=35,color='red',alpha =(0.9))
            # Fix posistion when display is added
        if got_money == True:
            screen.draw.text(f'You won money',(100,366),fontsize=30,color='green',alpha =(0.9))
            screen.draw.text(f'+ 1000 B',(65,30),fontsize=25,color="gold")
            # Fix posistion when display is added

    blorp.draw()
    

    # MENU
    if Menu == True and home == True:
        menu_background.draw()
        screen.draw.text('MENU',(625, 85,),fontsize=50,color='black')
        screen.draw.text('CLOSE [X]',(WIDTH/1.2, 85,),fontsize=25,color='red')
        screen.draw.text('SPEICAL BLORPS',(230, 170,),fontsize=35,color='black')
        screen.draw.text('Info: Speical blorps are unlocked by\nspinning the wheel at the casino.',(230, 200,),fontsize=20,color='darkgrey')
        
        if price_1 == False:
            screen.draw.text('Not owned',(285, 315,),fontsize=25,color='black')
            lock.draw() # 290,300
            blorp_preview_1.draw()
        else:
            screen.draw.text('Equip',(302, 296,),fontsize=25,color='silver')
            blorp_preview_1.draw()
            yes_button.draw()
            no_button.draw() 

        if price_2 == False:
            screen.draw.text('Not owned',(285, 440,),fontsize=25,color='black')
            lock2.draw() # 290,425
            blorp_preview_2.draw()
        else:
            screen.draw.text('Equip',(302, 412,),fontsize=25,color='silver')
            blorp_preview_2.draw()
            yes_button_2.draw()
            no_button_2.draw()
    
        if difficulty == True:
            screen.draw.text('Difficulty switch: ',(850, 400,),fontsize=25,color='black')
            screen.draw.text('Hard',(1000, 400,),fontsize=25,color='darkred')
            switch_hard.pos = (950,450) # Not smart but works
            switch_hard.draw()
            switch_easy.pos = (1,1) # Not smart but works
        else:
            screen.draw.text('Difficulty switch: ',(850, 400,),fontsize=25,color='black')
            screen.draw.text('Easy',(1000, 400,),fontsize=25,color='darkgreen')
            switch_easy.pos = (950,450) # Not smart but works
            switch_easy.draw()
            switch_hard.pos = (1,1) # Not smart but works

def on_mouse_down(pos,button): 
     global money
     global unlock_special
     global unlock_ultimate
     global blorp_select
     global blorp_color
     global timer
     global nothing,ultimate_blorp,gliched_blorp,got_money
    # Buy loot box
     if button == mouse.LEFT and wheel.collidepoint(pos) and home == True and Menu == False:
        if money >= 50 and timer >= 0.1:
            money -= 50
            timer = 0
            nothing = False
            ultimate_blorp = False
            gliched_blorp = False
            got_money = False
            loot_box()

        if money <= 50:
            print('You need more money!')

    # Select skin
    # SPEICAL BLORP
     if button == mouse.LEFT and yes_button.collidepoint(pos) and Menu == True and price_1 == True:
         unlock_special = True
         unlock_ultimate = False
     if button == mouse.LEFT and no_button.collidepoint(pos) and Menu == True and price_1 == True:
         unlock_special = False
         blorp_color = 1
         blorp_select = 'blorp_grey.png'
    # ULTIMATE BLORP
     if button == mouse.LEFT and yes_button_2.collidepoint(pos) and Menu == True and price_2 == True:
         unlock_ultimate = True
         unlock_special = False
     if button == mouse.LEFT and no_button_2.collidepoint(pos) and Menu == True and price_2 == True:
         unlock_ultimate = False
         blorp_color = 1
         blorp_select = 'blorp_grey.png'

     # DIFFICULTY SWITCH
     global difficulty 
     if button == mouse.LEFT and switch_easy.collidepoint(pos) and Menu == True:
        difficulty = True
        print('difficulty ON')
     if button == mouse.LEFT and switch_hard.collidepoint(pos) and Menu == True:
        difficulty = False
        print('difficulty OFF')

        
def loot_box():
    global unlock_special
    global gliched_blorp
    global unlock_ultimate
    global ultimate_blorp
    global nothing
    global got_money
    global price_1
    global price_2
    global timer
    global money
    spin_the_wheel = random.randint(1,1000)
    if spin_the_wheel == 1000: 
        gliched_blorp = True
        unlock_special = True
        price_1 = True
        timer = -2.9
    if spin_the_wheel in [100,110,120,130,140,150,160,170,180,190,200]:
        ultimate_blorp = True
        unlock_ultimate = True
        price_2 = True
        timer = -1.4
    if spin_the_wheel in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]:
        got_money = True
        money += 1000
        timer = -0.9
    elif spin_the_wheel != 1000 and spin_the_wheel not in [100,110,120,130,140,150,160,170,180,190,200]:
        nothing = True
        
def update(dt):
    ### COLLIDERECT

    ### NEXT LEVEL
    global map_level
    global money
    global clock
    global on_block
    global nothing,gliched_blorp,ultimate_blorp,got_money
    global timer
    global current_map
    timer += dt
    if timer >= 5:
        got_money = False
        nothing = False
        ultimate_blorp = False
        gliched_blorp = False
    ## GOLDEN PORTAL
    # MAP A
    if map_level == 2:
        row = int((blorp.y + 25)/ tile_size)
        column = int(blorp.x / tile_size)
        tile = pictures[map_a[row][column]]
        if tile == "portal_black.png":
            map_level = 1
            money += 25 # change value
            blorp.pos = (75,575)
            current_map.clear()
            current_map = base_map.copy()
        if tile == "block_pink.png" or tile == "block_dark_grey.png": #ADD BLOCK
            on_block = True
        else:
            on_block = False

    # MAP B
    if map_level == 3:
        row = int((blorp.y + 25)/ tile_size)
        column = int(blorp.x / tile_size)
        tile = pictures[map_b[row][column]]
        if tile == "portal_black.png":
            map_level = 1
            money += 50 # change value 
            blorp.pos = (75,575)
            current_map.clear()
            current_map = base_map.copy()
        if tile == "block_green.png" or tile == "block_dark_grey.png": #ADD BLOCK
            on_block = True
        else:
            on_block = False    
    # MAP C
    if map_level == 4:
        row = int((blorp.y + 25) / tile_size)
        column = int(blorp.x / tile_size)
        tile = pictures[map_c[row][column]]
        if tile == "portal_black.png":
            map_level = 1
            money += 100 # change value
            blorp.pos = (75,575)
            current_map.clear()
            current_map = base_map.copy()
        if tile == "block_purple.png" or tile == "block_dark_grey.png": #ADD BLOCK
            on_block = True
        else:
            on_block = False    

    ## Difficulty MAPS
    # DA
    if map_level == 5:
        row = int((blorp.y + 25) / tile_size)
        column = int(blorp.x / tile_size)
        tile = pictures[map_da[row][column]]
        if tile == "portal_black.png":
            map_level = 1
            money += 400 # change value
            blorp.pos = (75,575)
            current_map.clear()
            current_map = base_map.copy()
        #if tile == "block_void.png":
        #    blorp.pos = (75,575)
        if tile == "block_pink.png" or tile == "block_dark_grey.png": #ADD BLOCK
            on_block = True
        else:
            on_block = False   
    # DB
    if map_level == 6:
        row = int((blorp.y + 25) / tile_size)
        column = int(blorp.x / tile_size)
        tile = pictures[map_db[row][column]]
        if tile == "portal_black.png":
            map_level = 1
            money += 600 # change value
            blorp.pos = (75,575)
            current_map.clear()
            current_map = base_map.copy()
        if tile == "block_void.png":
            blorp.pos = (75,575)
        if tile == "block_green.png" or tile == "block_dark_grey.png": #ADD BLOCK
            on_block = True
        else:
            on_block = False   
    # DC
    if map_level == 7:
        row = int((blorp.y + 25) / tile_size)
        column = int(blorp.x / tile_size)
        tile = pictures[map_dc[row][column]]
        if tile == "portal_black.png":
            map_level = 1
            money += 1000 # change value
            blorp.pos = (75,575)
            current_map.clear()
            current_map = base_map.copy()
        if tile == "block_void.png":
            blorp.pos = (75,575)
        if tile == "block_purple.png" or tile == "block_dark_grey.png": #ADD BLOCK
            on_block = True
        else:
            on_block = False   
            
    ## PORTALS BASE MAP / where you enter from 'HOME'
    if map_level == 1:
            # Checking if hard mode is true or false
            if difficulty != True:
                row = int((blorp.y + 25) / tile_size)
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
            else: 
                row = int((blorp.y + 25) / tile_size)
                column = int(blorp.x / tile_size)
                tile = pictures[base_map[row][column]]
                if tile == "portal_pink.png": #CHANGE PORTAL
                    map_level = 5
                    blorp.pos = (75,575)
                    current_map.clear()
                    current_map = map_da.copy()

                if tile == "portal_green.png": #CHANGE PORTAL
                    map_level = 6
                    blorp.pos = (75,575)
                    current_map.clear()
                    current_map = map_db.copy()

                if tile == "portal_purple.png": #CHANGE PORTAL
                    map_level = 7
                    blorp.pos = (75,575)
                    current_map.clear()
                    current_map = map_dc.copy()

            
            if tile == "block_grey.png" or tile == "block_dark_grey.png" or tile == "block_red.png": #ADD BLOCK
                on_block = True
            else:
                on_block = False

            ### BUY SKINS - OPTAINING SKINS
            # Global blorps
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
            if not blorp_color == 2:
                if unlock_blue != True and money >= 50:
                    if tile == "blorp_blue.png":
                        blorp_color = 2
                        blorp_select = 'blorp_blue.png'
                        money -= 50
                        unlock_blue = True
                elif unlock_blue == True:
                    if tile == "blorp_blue.png":
                        blorp_color = 2
                        blorp_select = 'blorp_blue.png'
            # LIGHT BLUE
            if not blorp_color == 3:
                if unlock_light_blue != True and money >= 50:
                    if tile == "blorp_light_blue.png":
                        blorp_color = 3
                        blorp_select = 'blorp_light_blue.png'
                        money -= 50
                        unlock_light_blue = True
                elif unlock_light_blue == True:
                    if tile == "blorp_light_blue.png":
                        blorp_color = 3
                        blorp_select = 'blorp_light_blue.png'
            # GREEN
            if not blorp_color == 4:
                if unlock_green != True and money >= 50:
                    if tile == "blorp_green.png":
                        blorp_color = 4
                        blorp_select = 'blorp_green.png'
                        money -= 50
                        unlock_green = True
                elif unlock_green == True:
                    if tile == "blorp_green.png":
                        blorp_color = 4
                        blorp_select = 'blorp_green.png'
            # YELLOW
            if not blorp_color == 5:
                if unlock_yellow != True and money >= 50:
                    if tile == "blorp_yellow.png":
                        blorp_color = 5
                        blorp_select = 'blorp_yellow.png'
                        money -= 50
                        unlock_yellow = True
                elif unlock_yellow == True:
                    if tile == "blorp_yellow.png":
                        blorp_color = 5
                        blorp_select = 'blorp_yellow.png'
            # RED
            if not blorp_color == 6:
                if unlock_red != True and money >= 50:
                    if tile == "blorp_red.png":
                        blorp_color = 6
                        blorp_select = 'blorp_red.png'
                        money -= 50
                        unlock_red = True
                elif unlock_red == True:
                    if tile == "blorp_red.png":
                        blorp_color = 6
                        blorp_select = 'blorp_red.png'
            # MAGENTA
            if not blorp_color == 7:
                if unlock_megenta != True and money >= 50:
                    if tile == "blorp_magenta.png":
                        blorp_color = 7
                        blorp_select = 'blorp_magenta.png'
                        money -= 50
                        unlock_megenta = True
                elif unlock_megenta == True:
                    if tile == "blorp_magenta.png":
                        blorp_color = 7
                        blorp_select = 'blorp_magenta.png'
            # SPEICAL
            if unlock_special == True:
                blorp_color = 9
                blorp_select = 'blorp_glitch.png'
            # ULTIMATE
            if unlock_ultimate == True:
                blorp_color = 10
                blorp_select = 'blorp_ultimate.png'

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

    ## ON BLOCK IS TRUE OR FALSE
    # While not jumping
    if on_block == True:
            blorp.image = blorp_select

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
            if blorp_color == 9:
                blorp.image = 'blorp_glitch_jump.png' # CHANGE HERE TO JUMP
            if blorp_color == 10:
                blorp.image = 'blorp_ultimate_jump.png' # CHANGE HERE TO JUMP

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