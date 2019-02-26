#Jacob Wilson
#Allison Obourn
#csc110_1L
#project 10

from DrawingPanel import *
import random
PROP_PERC = 75

#This program simulates a fire spread using DrawingPanel.
def main():
    filename = input("Input file: ")
    file = open(filename)
    lines = file.readlines()
    land_state = populate_grid(lines)
    
    p = DrawingPanel(10 * len(land_state[0]), 10 *
                     len(land_state))
    fire = draw_simulation(p, land_state)

    while fire == True:
        land_state = fire_spread(land_state)
        fire = draw_simulation(p, land_state)

#This function creates of list of lists representing the initial
#state of the land.
def populate_grid(lines):
    land_state = []
    for line in lines:
        line = line.split()
        land_state.append(line)
    return land_state

#This fuction simulates the fire spreading. First, the function
#checks the state of the land. If there is a fire,
#the function will check the squares directly North, South,
#East, and West of the fire. If those squares contain
#burnable vegetation and generate a number
#lower than the propagation percentage, those squares catch on
#fire as well.
def fire_spread(land_state):
    land_state_copy = []
    for i in range(len(land_state)):
        land_state_copy.append(land_state[i].copy())
    
    for i in range(len(land_state_copy)):
        for j in range(len(land_state_copy[i])):
            if land_state[j][i] == '2':
                land_state_copy[j][i] = '0'
                if land_state[j - 1][i] == '1':
                    rand_num = random.randint(1, 100)
                    if rand_num < PROP_PERC:
                        land_state_copy[j - 1][i] = '2'
                        
                if land_state[j + 1][i] == '1':
                    rand_num = random.randint(1, 100)
                    if rand_num < PROP_PERC:
                        land_state_copy[j + 1][i] = '2'

                if land_state[j][i - 1] == '1':
                    rand_num = random.randint(1, 100)
                    if rand_num < PROP_PERC:
                        land_state_copy[j][i - 1] = '2'

                if land_state[j][i + 1] == '1':
                    rand_num = random.randint(1, 100)
                    if rand_num < PROP_PERC:
                        land_state_copy[j][i + 1] = '2'
                        
    land_state = land_state_copy
    return land_state

#This function provides the visual representation of the
#the fire spread. yellow squares = nothing,
#green squares = vegetation, and red squares = fire
def draw_simulation(p, new_land_state):
    p.clear()
    fire = False
    for i in range(len(new_land_state)):
        for j in range(len(new_land_state[i])):
            if new_land_state[j][i] == '0':
                p.fill_rect(10 * i, 10 * j, 10, 10, "yellow")

            elif new_land_state[j][i] == '1':
                p.fill_rect(10 * i, 10 * j, 10, 10, "green")

            elif new_land_state[j][i] == '2':
                fire = True
                p.fill_rect(10 * i, 10 * j, 10, 10, "red")

        
    p.sleep(100)
    return fire

main()
