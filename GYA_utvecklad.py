''' 
Game Title:     The Blorp Game  
About:          GYA - Funktions spel utvecklade, denna 
                version har alla funktioner och är fullt
                utvecklad som vi vill ha det.
Creators:       Rikard W, Sebastian B and Oscar K

Current Version: v.2.1.0 '''


## IMPORTS
import random
import pgzrun
import os

# Variables
HEIGHT = 650
WIDTH = 1250

difficulty = False

Menu = False 
Menu_value = 0
q_timer = 0

home = False

existing = True
dx, dy = 50, 50

tile_size = 50

map_level = 0
current_map = []
timer = 0
gliched_blorp = False
ultimate_blorp = False
nothing = False
got_money = False
money = 0
gambling = True
# Record time / speedruns
record = False
best_time_4 = 0
best_time_5 = 0
best_time_6 = 0
best_time_9 = 0
best_time_10 = 0
best_time_11 = 0
current_time = 0
## Checkmarks
green_checkmark = False
purple_checkmark = False
pink_checkmark = False
blue_checkmark = False
red_checkmark = False
cloud_checkmark = False
# Difficulty checkmarks
d_green_checkmark = False
d_purple_checkmark = False
d_pink_checkmark = False
d_blue_checkmark = False
d_red_checkmark = False
d_cloud_checkmark = False


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
print("Verison V.2.1.0")

timer = 0
clock = 2
on_block = True

### IMAGES/ACTORS
blorp_select = 'blorp_grey.png'
blorp = Actor(f'{blorp_select}',pos = (75,575))
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
skull = Actor('skull.png',pos=(875,625))
hard_red_blocks = Actor('blocks_hard.png',pos=(925,575))
# Lock
lock = Actor('lock.png',pos=(290,300))
lock2 = Actor('lock.png',pos=(290,425))
# checkmark
show_green_checkmark = Actor('checkmark_green.png',pos= (678,472))
show_purple_checkmark = Actor('checkmark_green.png',pos= (878,472))
show_pink_checkmark = Actor('checkmark_green.png',pos= (1078,472))
show_blue_checkmark = Actor('checkmark_green.png',pos= (778,422))
show_red_checkmark = Actor('checkmark_green.png',pos= (978,422))
show_cloud_checkmark = Actor('checkmark_green.png',pos= (978,422))
# hard checkmarks
d_show_green_checkmark = Actor('checkmark_red.png',pos= (678,472))
d_show_purple_checkmark = Actor('checkmark_red.png',pos= (878,472))
d_show_pink_checkmark = Actor('checkmark_red.png',pos= (1078,472))
d_show_blue_checkmark = Actor('checkmark_red.png',pos= (778,422))
d_show_red_checkmark = Actor('checkmark_red.png',pos= (978,422))
d_show_cloud_checkmark = Actor('checkmark_red.png',pos= (978,422))
# Other
casino_display = Actor('casino_display.png',pos = (175,375))
casino = Actor('sign_casino.png',pos = (300,100))
sign = Actor('sign_wood.png',pos = (875,75))
wheel = Actor('casino_wheel.png',pos = (175,200))
menu_background = Actor('menu.png',pos = (650,300))
crack = Actor('empty.png',pos = (550,100))
backgrounds = ['background_grey.png','background_pink.png','background_green.png','background_purple.png',
               'background_pink.png','background_green.png','background_purple.png','background_red.png',
               'background_blue.png','background_red.png','background_blue.png','background_cloud.png','background_cloud.png'
               ,'background_temple.png','background_temple.png','background_temple.png','background_boss.png']
pictures = ['empty.png','block_grey.png','block_pink.png','block_green.png','block_purple.png',
            'portal_pink.png','portal_green.png','portal_purple.png','portal_black.png',
            'blorp_blue.png','blorp_light_blue.png','blorp_green.png','blorp_yellow.png',
            'blorp_red.png','blorp_magenta.png', 'block_dark_grey.png','block_red.png', 'block_void.png',
            'block_lava.png','portal_red.png','block_blue.png','portal_blue.png','chain.png','block_cloud.png','portal_cloud.png'
            ,'block_temple_1.png','block_temple_2.png','block_temple_3.png','portal_temple.png']

# WORLD DATA
maps = [
[
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #25w, 13h 
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 16, 16, 16, 16, 16, 16, 16, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 22, 0, 22, 0, 22, 24, 22, 0, 22, 0, 22, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 22, 0, 22, 21, 22, 0, 22, 19, 22, 0, 22, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 22, 6, 22, 0, 22, 7, 22, 0, 22, 5, 22, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 15, 15, 15, 0, 15, 15, 15, 0, 15, 15, 15, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 1],
],

[
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
],

[
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
],

[
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
],

[
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
],

[
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
],

[
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
],

[
[18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18],
[18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 0, 0, 0, 0, 18, 0, 0, 0, 0, 0, 0, 18], 
[18, 0, 0, 18, 18, 0, 0, 18, 0, 0, 18, 0, 0, 18, 18, 0, 0, 18, 0, 0, 0, 18, 18, 0, 18], 
[18, 0, 18, 18, 0, 0, 18, 0, 0, 18, 0, 0, 18, 0, 0, 0, 0, 0, 0, 0, 18, 0, 0, 0, 18], 
[18, 0, 0, 18, 18, 0, 0, 0, 0, 18, 18, 0, 0, 0, 0, 18, 0, 0, 0, 18, 0, 0, 0, 18, 18], 
[18, 0, 0, 0, 18, 0, 18, 0, 0, 0, 18, 0, 18, 0, 0, 0, 0, 0, 0, 18, 0, 0, 0, 18, 18], 
[18, 0, 0, 0, 18, 0, 0, 0, 0, 18, 0, 0, 0, 0, 0, 0, 0, 18, 0, 0, 18, 0, 0, 0, 18], 
[18, 18, 0, 18, 18, 0, 0, 0, 0, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 0, 0, 18], 
[18, 0, 0, 18, 0, 0, 0, 0, 0, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18], 
[18, 8, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 0, 0, 0, 0, 0, 18, 0, 0, 18, 18], 
[18, 18, 0, 0, 0, 18, 0, 0, 0, 18, 0, 0, 0, 0, 0, 0, 0, 18, 0, 0, 0, 0, 0, 0, 18], 
[18, 0, 0, 18, 0, 0, 0, 0, 0, 18, 0, 0, 0, 0, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18], 
[18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18],
],

[
[20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
[20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 20, 20, 0, 0, 0, 20, 20], 
[20, 20, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 20, 8, 0, 0, 0, 20], 
[20, 0, 0, 20, 20, 0, 0, 0, 0, 0, 20, 0, 0, 20, 20, 20, 0, 0, 0, 20, 20, 20, 0, 0, 20], 
[20, 0, 20, 20, 0, 0, 0, 0, 20, 0, 20, 0, 0, 0, 20, 0, 0, 0, 0, 0, 20, 0, 0, 20, 20], 
[20, 0, 0, 20, 0, 0, 0, 0, 20, 0, 20, 20, 0, 0, 20, 0, 0, 0, 0, 0, 20, 0, 0, 0, 20], 
[20, 20, 0, 20, 0, 0, 0, 0, 20, 0, 0, 0, 0, 0, 20, 0, 0, 0, 0, 0, 0, 20, 20, 0, 20], 
[20, 0, 0, 20, 0, 0, 0, 0, 20, 0, 0, 0, 0, 20, 20, 20, 0, 0, 0, 0, 0, 0, 0, 0, 20], 
[20, 0, 20, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 20, 0, 0, 0, 0, 0, 20, 0, 20, 20], 
[20, 0, 0, 20, 0, 0, 0, 0, 20, 0, 0, 0, 20, 0, 20, 20, 20, 0, 0, 0, 0, 20, 0, 0, 20], 
[20, 20, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 20, 20, 20, 0, 20, 0, 0, 20, 0, 0, 20], 
[20, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 20, 20, 20, 20, 0, 0, 0, 0, 0, 20], 
[20, 20, 20, 20, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 20, 20, 20, 20, 20, 17, 17, 17, 17, 17, 17],
], 

[
[18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18],
[18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 0, 0, 0, 0, 17, 0, 0, 0, 0, 0, 0, 18], 
[18, 0, 0, 18, 18, 0, 0, 17, 0, 0, 18, 0, 0, 17, 18, 0, 0, 17, 0, 0, 0, 18, 18, 0, 18], 
[18, 0, 17, 18, 0, 0, 18, 0, 0, 18, 0, 0, 18, 0, 0, 0, 0, 0, 0, 0, 17, 0, 0, 0, 18], 
[18, 0, 0, 17, 18, 0, 0, 0, 0, 18, 18, 0, 0, 0, 0, 18, 0, 0, 0, 17, 0, 0, 0, 18, 18], 
[18, 0, 0, 0, 18, 0, 18, 0, 0, 0, 17, 0, 18, 0, 0, 0, 0, 0, 0, 17, 0, 0, 0, 18, 18], 
[18, 0, 0, 0, 18, 0, 0, 0, 0, 18, 0, 0, 0, 0, 0, 0, 0, 18, 0, 0, 18, 0, 0, 0, 18], 
[18, 17, 0, 17, 18, 0, 0, 0, 0, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 0, 0, 18], 
[18, 0, 0, 18, 0, 0, 0, 0, 0, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18], 
[18, 8, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 0, 0, 0, 0, 0, 18, 0, 0, 18, 18], 
[18, 18, 0, 0, 0, 18, 0, 0, 0, 18, 0, 0, 0, 0, 0, 0, 0, 18, 0, 0, 0, 0, 0, 0, 18], 
[18, 0, 0, 18, 0, 0, 0, 0, 0, 18, 0, 0, 0, 0, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18], 
[18, 18, 18, 18, 17, 17, 17, 17, 17, 18, 17, 17, 17, 17, 18, 17, 17, 17, 17, 17, 17, 17, 17, 17, 18],
],

[
[20, 20, 20, 17, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 17, 17, 20, 20, 20, 20, 20, 20],
[20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0, 20, 20], 
[20, 20, 0, 0, 0, 0, 0, 0, 0, 0, 17, 0, 0, 0, 0, 0, 0, 0, 0, 20, 8, 0, 0, 0, 20], 
[20, 0, 0, 17, 20, 0, 0, 0, 0, 0, 17, 0, 0, 20, 20, 20, 0, 17, 0, 20, 20, 0, 0, 17, 20], 
[20, 0, 20, 20, 0, 0, 0, 0, 20, 0, 17, 0, 0, 0, 20, 17, 17, 0, 0, 0, 20, 0, 0, 0, 20], 
[20, 0, 0, 20, 0, 0, 17, 0, 17, 0, 20, 20, 0, 0, 20, 17, 0, 0, 0, 17, 20, 20, 0, 0, 20], 
[20, 20, 0, 20, 0, 0, 0, 0, 17, 0, 0, 0, 0, 0, 20, 17, 17, 0, 20, 0, 0, 0, 0, 20, 20], 
[17, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 20, 20, 17, 0, 0, 0, 0, 0, 0, 0, 20], 
[17, 0, 20, 20, 0, 0, 17, 0, 0, 0, 0, 0, 0, 0, 20, 20, 17, 0, 0, 0, 0, 20, 0, 0, 20], 
[17, 0, 0, 20, 0, 0, 0, 0, 20, 0, 0, 0, 20, 0, 20, 20, 20, 0, 0, 0, 0, 20, 0, 0, 20], 
[20, 20, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 17, 0, 20, 20, 20, 17, 20, 17, 17, 20, 0, 0, 20], 
[20, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 20, 20, 20, 20, 17, 17, 20, 0, 0, 20], 
[20, 20, 20, 20, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 20, 20, 20, 20, 20, 20, 20, 20, 17, 17, 17],
],

[
[23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23],
[17, 0, 0, 0, 0, 0, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17], 
[17, 0, 0, 23, 0, 0, 23, 0, 0, 0, 0, 23, 0, 0, 0, 23, 0, 0, 0, 23, 0, 0, 0, 0, 17], 
[17, 0, 0, 23, 0, 0, 17, 0, 23, 17, 17, 17, 23, 17, 17, 17, 23, 17, 17, 17, 23, 17, 17, 8, 23], 
[23, 23, 0, 0, 17, 0, 17, 0, 0, 17, 0, 0, 0, 17, 0, 0, 0, 17, 0, 0, 0, 17, 23, 23, 23], 
[17, 0, 0, 23, 17, 0, 0, 23, 0, 17, 0, 23, 0, 17, 0, 23, 0, 17, 0, 23, 0, 17, 23, 17, 23], 
[23, 23, 0, 0, 17, 0, 0, 17, 0, 0, 0, 17, 0, 0, 0, 17, 0, 0, 0, 17, 0, 0, 0, 0, 23], 
[17, 0, 0, 23, 17, 0, 0, 17, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 0, 0, 23], 
[23, 23, 0, 0, 17, 17, 0, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23], 
[17, 0, 0, 23, 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 23], 
[23, 23, 0, 0, 17, 0, 0, 0, 0, 17, 0, 17, 0, 17, 0, 17, 0, 17, 0, 17, 0, 17, 0, 17, 23], 
[23, 0, 0, 0, 17, 0, 0, 0, 23, 0, 23, 0, 23, 0, 23, 0, 23, 0, 23, 0, 23, 0, 23, 0, 23], 
[23, 23, 23, 17, 23, 23, 17, 17, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23],
],

[ #easy mode for cloud
[23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23],
[23, 0, 0, 0, 0, 0, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23], 
[23, 0, 0, 23, 0, 0, 23, 0, 0, 23, 0, 23, 0, 0, 23, 0, 23, 0, 0, 23, 0, 0, 0, 0, 23], 
[23, 0, 0, 23, 0, 0, 23, 0, 23, 23, 0, 0, 0, 0, 0, 0, 0, 23, 23, 23, 23, 23, 23, 8, 23], 
[23, 23, 0, 0, 23, 0, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 0, 0, 0, 23, 23, 23, 23], 
[23, 0, 0, 23, 23, 0, 0, 23, 0, 23, 0, 23, 0, 0, 0, 23, 0, 23, 0, 23, 0, 23, 23, 23, 23], 
[23, 23, 0, 0, 23, 0, 0, 23, 0, 23, 0, 23, 0, 0, 0, 23, 0, 0, 0, 23, 0, 0, 0, 0, 23], 
[23, 0, 0, 23, 23, 0, 0, 23, 0, 0, 0, 23, 0, 0, 0, 23, 23, 23, 23, 23, 23, 23, 0, 0, 23], 
[23, 23, 0, 0, 23, 23, 0, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23], 
[23, 0, 0, 23, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 23], 
[23, 23, 0, 0, 23, 0, 0, 0, 0, 23, 0, 23, 0, 23, 0, 23, 0, 23, 0, 23, 0, 23, 0, 23, 23], 
[23, 0, 0, 0, 23, 0, 0, 0, 23, 0, 23, 0, 23, 0, 23, 0, 23, 0, 23, 0, 23, 0, 23, 0, 23], 
[23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23],
],

[ #temple 1
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
],

[ #temple 2
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
],

[ #temple 3
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
],

[ #boss room
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
],
]

current_map = maps[0].copy()

# OTHER-FUNKTIONS
#music
musics_sound = 0
def musics():
    if map_level == 0 or map_level == 1 or map_level == 2 or map_level == 3 or map_level == 7 or map_level == 8 or map_level == 12:
        music_sound = 0
        music.stop()
    if map_level == 1 or map_level == 2 or map_level == 3 or map_level == 7 or map_level == 8 or map_level == 12:
        music_sound = 0
        music.stop()
    if map_level == 4 or map_level == 5 or map_level == 6 or map_level == 9 or map_level == 10 or map_level == 11:
        music_sound = 2
        music.stop()
    if music_sound == 0 and music_stop == False:
        music.play("home.wav")

    if music_sound == 2 and music_stop == False:
        music.play("hard.wav")


def draw_grid():
    '''draw a nXn grid'''
    x,y = 0,0

    for _ in range(tile_size+1):
        screen.draw.line((x,0),(x,HEIGHT),'red')
        screen.draw.line((0,y),(WIDTH,y),'red')
        x += dx 
        y += dy 

def draw_tiles():
    selected_map = maps[map_level]  
    for row in range(len(selected_map)):
        for column in range(len(selected_map[row])):
            x = column * tile_size
            y = row * tile_size
            tile = pictures[selected_map[row][column]]
            screen.blit(tile, (x, y))

def possible_move(deltax,deltay):
    global r,current_time
    blorp.x += deltax
    blorp.y += deltay
    for ri,row in enumerate(current_map):
        for ci,tile in enumerate(row):
                if tile and not tile in [5,6,7,8,9,10,11,12,13,14,19,21,22,24]:
                    # Smaller rect than tile 
                    r = Rect(ci*dx+5,ri*dy+5,dx-10,dy-10)
                    if blorp.colliderect(r):
                        #print(r,blorp.pos,tile)
                        blorp.x -= deltax
                        blorp.y -= deltay
                        if tile == 17:
                            blorp.x = 75
                            blorp.y = 575
                            sounds.death.play()
                            current_time = 0

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
    screen.blit(backgrounds[map_level],(0,0))

    #draw_grid()  
    draw_tiles()

    # Display exit button
    if home != True:
        screen.draw.text('Exit [B]',(20,15),color="darkred",alpha=(0.8))
    
    # records
    if map_level == 4 or map_level == 5 or map_level == 6 or map_level == 9 or map_level == 10 or map_level == 11:
        screen.draw.text(f'{current_time:.3f}',centerx=WIDTH/2,centery=20,fontsize=40,color="black")

    ### HOME 
    # HOME BASE TEXT
    if home == True:
        screen.draw.text('ENTER A PORTAL TO BEGIN!',(600,310),fontsize=55,color="darkgrey",alpha=0.4)
        screen.draw.text(f'Money : {money} B',(10,10),fontsize=25,color="gold")
        wheel.draw()
        casino.draw()
        sign.draw()
        screen.draw.text('COSMETICS',(760,60),fontsize=55,color='black',alpha=0.6)
        screen.draw.text('Press [Q] to open the Menu',(100,610),fontsize=25,color='darkgrey',alpha=0.7)
        screen.draw.text(f'50 B',(160,75),fontsize=25,color="gold")

        ## Hard mode display
        
        #We might add this, right now it's on hold.
        if difficulty == False:
            if green_checkmark == True:
                show_green_checkmark.draw()
            if purple_checkmark == True:
                show_purple_checkmark.draw()
            if pink_checkmark == True:
                show_pink_checkmark.draw()
            if blue_checkmark == True:
                show_blue_checkmark.draw()
            if red_checkmark == True:
                show_red_checkmark.draw()
            if cloud_checkmark == True:
                show_cloud_checkmark.draw()

        if difficulty == True:
            hard_red_blocks.draw()
            skull.draw()
            if d_green_checkmark == True:
                d_show_green_checkmark.draw()
            if d_purple_checkmark == True:
                d_show_purple_checkmark.draw()
            if d_pink_checkmark == True:
                d_show_pink_checkmark.draw()
            if d_blue_checkmark == True:
                d_show_blue_checkmark.draw()
            if d_red_checkmark == True:
                d_show_red_checkmark.draw()
            if d_cloud_checkmark == True:
                d_show_cloud_checkmark.draw()
            #screen.draw.text('Hard mode active',(850,610),fontsize=45,color="darkred")
        
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

        # SCREEN OF DISPLAY         x-y = (175,375)
        if gliched_blorp == True:
            screen.draw.text(f'You won "GLITCHED BLORP"',(96,368),fontsize=17,color='purple',alpha = (0.9))
            
        if ultimate_blorp == True:
            screen.draw.text(f'You won "ULTIMATE BLORP"',(96,368),fontsize=17,color='pink',alpha = (0.9)) 
            
        if nothing == True:
            screen.draw.text(f'You lost',(125,363),fontsize=35,color='red',alpha =(0.9))
            
        if got_money == True:
            screen.draw.text(f'You won money',(100,366),fontsize=30,color='green',alpha =(0.9))
            screen.draw.text(f'+ 1000 B',(65,30),fontsize=25,color="gold")
            

    blorp.draw()

    # MENU
    if Menu == True and home == True:
        menu_background.draw()
        screen.draw.text('MENU',(625, 85,),fontsize=50,color='black')
        screen.draw.text('CLOSE [Q]',(WIDTH/1.2, 85,),fontsize=25,color='red')
        screen.draw.text('SPEICAL BLORPS',(230, 170,),fontsize=35,color='black')
        screen.draw.text('Info: Speical blorps are unlocked by\nspinning the wheel at the casino.',(230, 200,),fontsize=20,color='darkgrey')
        
        # Records!
        global best_time_4,best_time_5,best_time_6,best_time_9,best_time_10,best_time_11
        screen.draw.text('All records',(750, 170,),fontsize=25,color='black')
        screen.draw.text('Hard mode only',(750, 135,),fontsize=30,color='darkred')
        if best_time_5 == 0:
            screen.draw.text(f'Green map | Time : N/A',(750, 190,),fontsize=25,color='black')
        else:
            screen.draw.text(f'Green map | Time : {best_time_5:.3f} seconds',(750, 190,),fontsize=25,color='green')
        
        if best_time_6 == 0:
            screen.draw.text(f'Purple map | Time : N/A',(750, 210,),fontsize=25,color='black')
        else:
            screen.draw.text(f'Purple map | Time : {best_time_6:.3f} seconds',(750, 210,),fontsize=25,color='purple')

        if best_time_4 == 0:
            screen.draw.text(f'Pink map | Time : N/A',(750, 230,),fontsize=25,color='black')
        else:
            screen.draw.text(f'Pink map | Time : {best_time_4:.3f} seconds',(750, 230,),fontsize=25,color='pink')

        if best_time_10 == 0:
            screen.draw.text(f'Blue map | Time : N/A',(750, 250,),fontsize=25,color='black')
        else:
            screen.draw.text(f'Blue map | Time : {best_time_10:.3f} seconds',(750, 250,),fontsize=25,color='blue')

        if best_time_9 == 0:
            screen.draw.text(f'Red map | Time : N/A',(750, 270,),fontsize=25,color='black')
        else:
            screen.draw.text(f'Red map | Time : {best_time_9:.3f} seconds',(750, 270,),fontsize=25,color='red')

        if best_time_11 == 0:
            screen.draw.text(f'Cloud map | Time : N/A',(750, 290,),fontsize=25,color='black')
        else:
            screen.draw.text(f'Cloud map | Time : {best_time_9:.3f} seconds',(750, 290,),fontsize=25,color='white')


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
        sounds.switch.play()
     if button == mouse.LEFT and switch_hard.collidepoint(pos) and Menu == True:
        difficulty = False
        sounds.switch.play()

        
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
        sounds.win.play()
    if spin_the_wheel in [100,110,120,130,140,150,160,170,180,190,200]:
        ultimate_blorp = True
        unlock_ultimate = True
        price_2 = True
        timer = -1.4
        sounds.win.play()
    if spin_the_wheel in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]: 
        got_money = True
        money += 1000
        timer = -0.9
        sounds.win.play()
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
    ### Records
    global current_time,best_time_4,best_time_5,best_time_6,best_time_9,best_time_10,best_time_11,record
    current_time += dt
    if map_level == 0:
        current_time = 0
    ## Music


    ## GOLDEN PORTAL
    # MAP PINK
    if map_level == 1:
        row = int((blorp.y + 25)/ tile_size)
        column = int(blorp.x / tile_size)
        tile = pictures[maps[1][row][column]]
        if tile == "portal_black.png":
            map_level = 0
            money += 100 # change value
            blorp.pos = (75,575)
            current_map.clear()
            current_map = maps[0].copy()
            #music
            musics()
            #checkmark
            global pink_checkmark
            pink_checkmark = True
            sounds.complete_level.play()
        if tile == "block_pink.png" or tile == "block_dark_grey.png": #ADD BLOCK
            on_block = True
        else:
            on_block = False

    # MAP GREEN
    if map_level == 2:
        row = int((blorp.y + 25)/ tile_size)
        column = int(blorp.x / tile_size)
        tile = pictures[maps[2][row][column]]
        if tile == "portal_black.png":
            map_level = 0
            money += 50 # change value 
            blorp.pos = (75,575)
            current_map.clear()
            current_map = maps[0].copy()
            #music
            musics()
            # checkmark
            global green_checkmark
            green_checkmark = True
            sounds.complete_level.play()
            music.stop()
        if tile == "block_green.png" or tile == "block_dark_grey.png": #ADD BLOCK
            on_block = True
        else:
            on_block = False    
    # MAP PURPLE
    if map_level == 3:
        row = int((blorp.y + 25) / tile_size)
        column = int(blorp.x / tile_size)
        tile = pictures[maps[3][row][column]]
        if tile == "portal_black.png":
            map_level = 0
            money += 80 # change value
            blorp.pos = (75,575)
            current_map.clear()
            current_map = maps[0].copy()
            #music
            musics()
            # checkmark
            global purple_checkmark
            purple_checkmark = True
            sounds.complete_level.play()
        if tile == "block_purple.png" or tile == "block_dark_grey.png": #ADD BLOCK
            on_block = True
        else:
            on_block = False    

    #MAP RED
    if map_level == 7:
        row = int((blorp.y + 25) / tile_size)
        column = int(blorp.x / tile_size)
        tile = pictures[maps[7][row][column]]
        if tile == "portal_black.png":
            map_level = 0
            money += 250 # change value
            blorp.pos = (75,575)
            current_map.clear()
            current_map = maps[0].copy()
            #music
            musics()
            # checkmark
            global red_checkmark
            red_checkmark = True
            sounds.complete_level.play()
        if tile == "block_lava.png": #ADD BLOCK
            on_block = True
        else:
            on_block = False  

    #MAP BLUE
    if map_level == 8:
        row = int((blorp.y + 25) / tile_size)
        column = int(blorp.x / tile_size)
        tile = pictures[maps[8][row][column]]
        if tile == "portal_black.png":
            map_level = 0
            money += 220 # change value
            blorp.pos = (75,575)
            current_map.clear()
            current_map = maps[0].copy()
            #music
            musics()
            # checkmark
            global blue_checkmark
            blue_checkmark = True
            sounds.complete_level.play()
        if tile == "block_blue.png": #ADD BLOCK
            on_block = True
        else:
            on_block = False  
    #MAP CLOUD
    if map_level == 12:
        row = int((blorp.y + 25) / tile_size)
        column = int(blorp.x / tile_size)
        tile = pictures[maps[12][row][column]]
        if tile == "portal_black.png":
            map_level = 0
            money += 450 # change value
            blorp.pos = (75,575)
            current_map.clear()
            current_map = maps[0].copy()
            #music
            musics()
            # checkmark
            global cloud_checkmark
            cloud_checkmark = True
            sounds.complete_level.play()
        if tile == "block_cloud.png": #ADD BLOCK
            on_block = True
        else:
            on_block = False  


    ## Difficulty MAPS
    # pink
    if map_level == 4:
        row = int((blorp.y + 25) / tile_size)
        column = int(blorp.x / tile_size)
        tile = pictures[maps[4][row][column]]
        if tile == "portal_black.png":
            map_level = 0
            money += 1000 # change value
            blorp.pos = (75,575)
            current_map.clear()
            current_map = maps[0].copy()
            #music
            musics()
            # checkmark
            global d_pink_checkmark
            d_pink_checkmark = True
            # records
            if current_time < best_time_4 and not best_time_4 == 0:
                best_time_4 = current_time
            elif best_time_4 == 0:
                best_time_4 = current_time
            print(best_time_4)
        #if tile == "block_void.png":
        #    blorp.pos = (75,575)
        if tile == "block_pink.png" or tile == "block_dark_grey.png": #ADD BLOCK
            on_block = True
        else:
            on_block = False   
    # green
    if map_level == 5:
        row = int((blorp.y + 25) / tile_size)
        column = int(blorp.x / tile_size)
        tile = pictures[maps[5][row][column]]
        if tile == "portal_black.png":
            map_level = 0
            money += 500 # change value
            blorp.pos = (75,575)
            current_map.clear()
            current_map = maps[0].copy()
            #music
            musics()
            # checkmark
            global d_green_checkmark
            d_green_checkmark = True
            # records
            if current_time < best_time_5 and not best_time_5 == 0:
                best_time_5 = current_time
            elif best_time_5 == 0:
                best_time_5 = current_time
            print(best_time_5)
        if tile == "block_void.png":
            blorp.pos = (75,575)
            current_time = 0
        if tile == "block_green.png" or tile == "block_dark_grey.png": #ADD BLOCK
            on_block = True
        else:
            on_block = False   
    # purple
    if map_level == 6:
        row = int((blorp.y + 25) / tile_size)
        column = int(blorp.x / tile_size)
        tile = pictures[maps[6][row][column]]
        if tile == "portal_black.png":
            map_level = 0
            money += 860 # change value
            blorp.pos = (75,575)
            current_map.clear()
            current_map = maps[0].copy()
            #music
            musics()
            # checkmark
            global d_purple_checkmark
            d_purple_checkmark = True
            # records
            if current_time < best_time_6 and not best_time_6 == 0:
                best_time_6 = current_time
            elif best_time_6 == 0:
                best_time_6 = current_time
            print(best_time_6)
        if tile == "block_void.png":
            blorp.pos = (75,575)
            current_time = 0
        if tile == "block_purple.png" or tile == "block_dark_grey.png": #ADD BLOCK
            on_block = True
        else:
            on_block = False   

    # Dif.blue
    if map_level == 10:
        row = int((blorp.y + 25) / tile_size)
        column = int(blorp.x / tile_size)
        tile = pictures[maps[10][row][column]]
        if tile == "portal_black.png":
            map_level = 0
            money += 1440 # change value
            blorp.pos = (75,575)
            current_map.clear()
            current_map = maps[0].copy()
            #music
            musics()
            # checkmark
            global d_blue_checkmark
            d_blue_checkmark = True
            # records
            if current_time < best_time_10 and not best_time_10 == 0:
                best_time_10 = current_time
            elif best_time_10 == 0:
                best_time_10 = current_time
            print(best_time_10)
        if tile == "block_void.png":
            blorp.pos = (75,575)
            current_time = 0
        if tile == "block_blue.png" or tile == "block_dark_grey.png": #ADD BLOCK
            on_block = True
        else:
            on_block = False   

    # Dif.red
    if map_level == 9:
        row = int((blorp.y + 25) / tile_size)
        column = int(blorp.x / tile_size)
        tile = pictures[maps[9][row][column]]
        if tile == "portal_black.png":
            map_level = 0
            money += 2500 # change value
            blorp.pos = (75,575)
            current_map.clear()
            current_map = maps[0].copy()
            #music
            musics()
            # checkmark
            global d_red_checkmark
            d_red_checkmark = True
            # records
            if current_time < best_time_9 and not best_time_9 == 0:
                best_time_9 = current_time
            elif best_time_9 == 0:
                best_time_9 = current_time
            print(best_time_9)
        if tile == "block_void.png":
            blorp.pos = (75,575)
            current_time = 0
        if tile == "block_lava.png" or tile == "block_dark_grey.png": #ADD BLOCK
            on_block = True
        else:
            on_block = False   

    # Dif.cloud
    if map_level == 11:
        row = int((blorp.y + 25) / tile_size)
        column = int(blorp.x / tile_size)
        tile = pictures[maps[11][row][column]]
        if tile == "portal_black.png":
            map_level = 0
            money += 2500 # change value
            blorp.pos = (75,575)
            current_map.clear()
            current_map = maps[11].copy()
            #music
            musics()
            # checkmark
            global d_cloud_checkmark
            d_cloud_checkmark = True   
            # records
            if current_time < best_time_11 and not best_time_11 == 0:
                best_time_11 = current_time
            elif best_time_11 == 0:
                best_time_11 = current_time
            print(best_time_11)
        if tile == "block_void.png":
            blorp.pos = (75,575)
            current_time = 0
        if tile == "block_cloud.png":
            on_block = True
        else:
            on_block = False 
            
    ## PORTALS BASE MAP / where you enter from 'HOME'
    if map_level == 0:
            # Checking if hard mode is true or false
            if difficulty != True:
                row = int((blorp.y + 25) / tile_size)
                column = int(blorp.x / tile_size)
                tile = pictures[maps[0][row][column]]
                if tile == "portal_pink.png": #CHANGE PORTAL
                    map_level = 1
                    blorp.pos = (75,575)
                    current_map.clear()
                    current_map = maps[1].copy()
                    sounds.teleport.play()
                    #music
                    musics()

                if tile == "portal_green.png": #CHANGE PORTAL
                    map_level = 2
                    blorp.pos = (75,575)
                    current_map.clear()
                    current_map = maps[2].copy()
                    sounds.teleport.play()
                    #music
                    musics()

                if tile == "portal_purple.png": #CHANGE PORTAL
                    map_level = 3
                    blorp.pos = (75,575)
                    current_map.clear()
                    current_map = maps[3].copy()
                    sounds.teleport.play()
                    #music
                    musics()

                if tile == "portal_red.png": #CHANGE PORTAL
                    map_level = 7
                    blorp.pos = (75,575)
                    current_map.clear()
                    current_map = maps[7].copy()
                    sounds.teleport.play()
                    #music
                    musics()

                if tile == "portal_blue.png": #CHANGE PORTAL
                    map_level = 8
                    blorp.pos = (75,575)
                    current_map.clear()
                    current_map = maps[8].copy()
                    sounds.teleport.play()
                    #music
                    musics()
                
                if tile == "portal_cloud.png": #CHANGE PORTAL
                    map_level = 12
                    blorp.pos = (75,575)
                    current_map.clear()
                    current_map = maps[12].copy()
                    sounds.teleport.play()
                    #music
                    musics()

            else: 
                row = int((blorp.y + 25) / tile_size)
                column = int(blorp.x / tile_size)
                tile = pictures[maps[0][row][column]]
                if tile == "portal_pink.png": #CHANGE PORTAL
                    map_level = 4
                    blorp.pos = (75,575)
                    current_map.clear()
                    current_map = maps[4].copy()
                    sounds.teleport.play()
                    #music
                    musics()

                if tile == "portal_green.png": #CHANGE PORTAL
                    map_level = 5
                    blorp.pos = (75,575)
                    current_map.clear()
                    current_map = maps[5].copy()
                    sounds.teleport.play()
                    #music
                    musics()

                if tile == "portal_purple.png": #CHANGE PORTAL
                    map_level = 6
                    blorp.pos = (75,575)
                    current_map.clear()
                    current_map = maps[6].copy()
                    sounds.teleport.play()
                    #music
                    musics()

                if tile == "portal_blue.png": #CHANGE PORTAL
                    map_level = 10
                    blorp.pos = (75,575)
                    current_map.clear()
                    current_map = maps[10].copy()
                    sounds.teleport.play()
                    #music
                    musics()
                
                if tile == "portal_red.png": #CHANGE PORTAL
                    map_level = 9
                    blorp.pos = (75,575)
                    current_map.clear()
                    current_map = maps[9].copy()
                    sounds.teleport.play()
                    #music
                    musics()

                if tile == "portal_cloud.png": #CHANGE PORTAL
                    map_level = 11
                    blorp.pos = (75,575)
                    current_map.clear()
                    current_map = maps[11].copy()
                    sounds.teleport.play()
                    #music
                    musics()

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
                        sounds.buy.play()
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
                        sounds.buy.play()
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
                        sounds.buy.play()
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
                        sounds.buy.play()
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
                        sounds.buy.play()
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
                        sounds.buy.play()
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
        sounds.jump.play()
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
    global q_timer
    q_timer += dt
    if keyboard.Q and Menu != True and q_timer > 0.3:
        Menu = True
        q_timer = 0
    if keyboard.Q and Menu != False and q_timer > 0.5:
        Menu = False
        q_timer = 0

    ### HOME
    global home
    if map_level == 0:
        home = True
    else:
        home = False

    if keyboard.B and home == False:
        blorp.pos = (75,575)
        current_map.clear()
        current_map = maps[0].copy()
        map_level = 0
        musics()    

    ### LOOT BOXES
    global loot
    global spin_the_wheel

## END-CODE
#MUSIC
music_stop = False
music_true = True
if music_true == True:
    music.play("home.wav")
    music_true = False
#SCREEN
os.environ['SDL_VIDEO_CENTERED'] = '1'
pgzrun.go()