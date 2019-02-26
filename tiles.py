#Jacob Wilson
#Allison Obourn
#csc110_1L
#project 9

from DrawingPanel import *
import random
PANEL_HEIGHT = 500
PANEL_WIDTH = 500
p = DrawingPanel(PANEL_WIDTH, PANEL_HEIGHT)
tile_list = []

#This program draws 50 tiles of random location, random size, and random
#color. The program then responds to user commands to either: raise a tile,
#lower a tile, delete a single tile, delete all the tiles, add a tile,
#or shuffle the tiles.
def main():    
    p.window.bind("<Button-1>", raises)
    p.window.bind("<Button-3>", lower)
    p.window.bind("<Button-2>", lower)
    p.window.bind("<Shift-Button-1>", delete)
    p.window.bind("<Shift-Button-3>", delete_all)
    p.window.bind("<Shift-Button-2>", delete_all)
    p.window.bind("<s>", shuffle)
    p.window.bind("<n>", add)
    add_all()
    draw_all()
    
#This function contains the code to produce a single random tile    
def add(event):
    rand_width = random.randint(25, 60)
    rand_height = random.randint(25, 60)
    rand_x = random.randint(0, PANEL_WIDTH - rand_width)
    rand_y = random.randint(0, PANEL_HEIGHT - rand_height)
    color = (random.randint(0, 255), random.randint(0, 255),
             random.randint(0, 255))
    
    tuple_list = (rand_x, rand_y, rand_width, rand_height, color)

    tile_list.append(tuple_list)
    draw_all()
    
#This function creates the orginal 50 tiles and then allows the user to
#create a new tile by pressing the "n" key.
def add_all():
    for i in range(50):
        add(None)

#This function clears the panel and redraws the tiles each time the
#function is called.
def draw_all():
    p.clear()
    for i in range(len(tile_list)):
        p.fill_rect(tile_list[i][0], tile_list[i][1], tile_list[i][2],
                    tile_list[i][3], tile_list[i][4])
        
#This function brings the clicked on tile up from the back of the panel
#to the front. Executed by appending said tile to the end of the list. 
def raises(event):
    x_coord = event.x
    y_coord = event.y
    for i in range(len(tile_list)-1, 0, -1):
        if (x_coord <= tile_list[i][0] + tile_list[i][2]
            and x_coord >= tile_list[i][0] and y_coord <= tile_list[i][1]
            + tile_list[i][3] and y_coord >= tile_list[i][1]):
             click = tile_list[i]
             tile_list.remove(click)
             tile_list.append(click)
             break           
    draw_all()

#This function pushes the clicked on tile from the front of the panel
#to the back. Executed by inserting said tile to the front of the list.             
def lower(event):
    x_coord = event.x
    y_coord = event.y
    for i in range(len(tile_list)-1, 0, -1):
        if (x_coord <= tile_list[i][0] + tile_list[i][2]
            and x_coord >= tile_list[i][0] and y_coord <= tile_list[i][1]
            + tile_list[i][3] and y_coord >= tile_list[i][1]):
            click = tile_list[i]
            tile_list.remove(click)
            tile_list.insert(0, click)
            break             
    draw_all()

#This function deletes the specific tile being clicked on.        
def delete(event):
    x_coord = event.x
    y_coord = event.y
    for i in range(len(tile_list)-1, 0, -1):
        if (x_coord <= tile_list[i][0] + tile_list[i][2]
            and x_coord >= tile_list[i][0] and y_coord <= tile_list[i][1]
            + tile_list[i][3] and y_coord >= tile_list[i][1]):
            click = tile_list[i]
            tile_list.remove(click)
            break
    draw_all()

#This function deletes all tiles in the panel.
def delete_all(event):
    x_coord = event.x
    y_coord = event.y
    for i in range(len(tile_list)-1, 0, -1):
        if (x_coord <= tile_list[i][0] + tile_list[i][2]
            and x_coord >= tile_list[i][0] and y_coord <= tile_list[i][1]
            + tile_list[i][3] and y_coord >= tile_list[i][1]):
            click = tile_list[i]
            tile_list.clear()
            break
    draw_all()
    
#This function shuffles all tiles into new x and y coordinates but does
#not alter the size or color of the tile.
def shuffle(event):
    tuple_list = []
    for i in range(len(tile_list)):
        
        rand_x = random.randint(0, PANEL_WIDTH - tile_list[i][2])
        rand_y = random.randint(0, PANEL_HEIGHT - tile_list[i][3])
        new_tuple_list = (rand_x, rand_y, tile_list[i][2], tile_list[i][3], tile_list[i][4])
        tile_list[i] = new_tuple_list    
    draw_all()
    
main()
    
