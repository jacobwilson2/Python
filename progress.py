#Jacob Wilson
#csc110_1L
#Project3

from DrawingPanel import *
import random


# This program prompts the user to type in how many steps they have walked
# the program draws a full flower with 10 leaves for every 5000 steps taken and 
# a  partial flower with two leaves for every 1000 steps taken

def main():
    steps = int(input("How many steps have you walked?"))
    number_flower = (steps // 5000)
    steps_remaining = (steps % 5000) // 1000
    panel = DrawingPanel(500, 300)

    # Background
    panel.fill_rect(0, 275, 500, 25, "dark green")
    panel.fill_rect(0, 75, 500, 200, "sky blue")
    panel.fill_rect(0, 0, 500, 75, "steel blue")
    panel.fill_oval(-50, -50, 150, 150, "gold")
    panel.fill_oval(150, 33, 100, 75, "gray75")
    panel.fill_oval(225, 33, 100, 75, "gray75")
    panel.fill_oval(300, 33, 100, 75, "gray75")

    # Draw flowers
    for i in range(number_flower):
        x = random.randint(40, 460)
        panel.set_stroke(5)
        panel.draw_line(x, 300, x, 180, "forest green")
        panel.fill_oval(x - 25, 130, 50, 50, "yellow")
        panel.fill_oval(x - 5, 151, 10, 10, "red")
        for i in range(1,6):
            panel.draw_line(x, 20 * i + 190, x + 10, 20 * i + 180, "forest green")
            panel.draw_line(x, 20 * i + 180, x - 10, 20 * i + 170, "forest green")


    
    if(steps_remaining > 0):
        x = random.randint(40, 460)
        panel.set_stroke(5)
        panel.draw_line(x, (300 - (steps_remaining * 20 + 20)), x, 300, "forest green")
        for i in range(0,steps_remaining):
            panel.draw_line(x,290 - (20 * i), x + 10,280 - (20 * i), "forest green")
            panel.draw_line(x, 280 - (20 * i), x - 10,270 - (20 * i), "forest green")
        panel.fill_oval(x - 25, 230 - (20 * steps_remaining), 50, 50, "yellow")
        panel.fill_oval(x - 5, 251 - (20 * steps_remaining), 10, 10, "red")
        
main()
