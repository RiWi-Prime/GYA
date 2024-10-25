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

# IMAGES/ACTORS
blorp_grey = Actor('blorp_grey.png')
i0 = Actor('test_bg2.png')
i1 = Actor('test_bg3.png')
existing = True

## CODE
game = True
print("game")
timer = 0
tile_list = []

'''
class World():
	def __init__(self, data):

		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 1:
					img = (dirt_image, (tile_size, tile_size))
					img_rect = (tile_size, tile_size)
					#img_rect.x = col_count * tile_size
					#img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					tile_list.append(tile)
				if tile == 2:
					img = (grass_image, (tile_size, tile_size))
					img_rect = (tile_size, tile_size)
					#img_rect.x = col_count * tile_size
					#img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					tile_list.append(tile)
				col_count += 1
			row_count += 1
'''


world_data = [
[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #25w, 13h
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  
[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

#world = World(world_data)

# OTHER-FUNKTIONS
'''Other funktions should placed here'''

def draw_grid():
	for line in range(0, 30):
		screen.draw.line((0, line * tile_size), (WIDTH, line * tile_size), (255, 255, 255))
		screen.draw.line((line * tile_size, 0), (line * tile_size, HEIGHT), (255, 255, 255))

def draw_world():
	for tile in tile_list:
		tile[0][0].draw()

# FUNKTIONS
def draw():
    ### BASIC DRAW (screen clear/blit/draw ect...)
    screen.clear()
    screen.blit('test_bg1.png',(0,0))
    blorp_grey.draw()
    draw_grid()
    draw_world()



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