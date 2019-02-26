#Jacob Wilson
#Csc110_1L
#Project_4

from DrawingPanel import * # so that I can use Graphics

#This function opens drawing panel and draws several layers
#of black and white squares to form and optical illusion
def main():
    panel = DrawingPanel(650, 400, background = "gray")
    draw_row(panel, 0,0 , 4, 20)
    draw_row(panel, 50, 70, 5, 30)
    draw_grid(panel, 10, 150, 4, 25, 8, 0)
    draw_grid(panel, 250, 200, 3, 25, 6, 10)
    draw_grid(panel, 425, 180, 5, 20, 10, 10)
    draw_grid(panel, 400, 20, 2, 35, 4, 35)
    
#This function draws one row of squares
#x: initial x position
#y: initial y position
#pairs: quantity of black and whire square pairs in row
#size: size of each square
def draw_row(panel, x, y, pairs, size):
    for i in range(0,pairs):
            panel.fill_rect(x, y, size, size, "black")
            panel.draw_line(x, y, x + size, y + size, "blue") 
            panel.draw_line(x + size, y, x, y + size, "blue")
            x += size
            panel.fill_rect(x, y, size, size, "white")
            x += size

#This function draws a grid
#height: quantity of rows being drawn in the grid
#offset: how far each second row is offset from the first
def draw_grid(panel, x, y, pairs, size, height, offset):
    for i in range(height):
        if i % 2 == 0:
            draw_row(panel, x, y + (size + 2) * i, pairs, size)

        else:
            draw_row(panel, x + offset, y + (size + 2) * i, pairs, size)

            
    
           
main()
