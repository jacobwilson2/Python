#Jacob Wilson
#Allison Obourn
#csc110_1L
#project 11

STRINGS = ["e", "B", "G", "D", "A", "E"]
NUM_SOLO_NOTES = 24
import random

#This Program prints some lyrics by Post Malone, then reads two sepearate text
#files. The program then asks for user input and generates a random chord
#progression and random notes for a solo. The program then prints the solo notes
#on a music staff
def main():
    intro()
    chord_dict, fret_dict = process_files()
    desired_key, num_unique_chords = obtain_input()
    create_chord_progression(desired_key, num_unique_chords,
                             chord_dict)
    solo_notes = solo_note_generator(desired_key, fret_dict)
    solo_list = create_solo_list(STRINGS, solo_notes)
    draw_staff(solo_list)
        
#This function prints a lyrical masterpiece by Post Malone.
def intro():
    print("Saucin', saucin', I'm saucin' on you")
    print("I'm swaggin', I'm swaggin', I'm swaggin' oh ooh")
    print("I'm ballin', I'm ballin', Iverson on you")
    
#This function asks the user for a desired key and number of
#unique chords. The function then returns user input.
def obtain_input():
    desired_key = input("What key would you like to play in ")
    num_unique_chords = int(input("How many unique chords? (up to 6) "))
    return desired_key, num_unique_chords

#This function reads both a chords and notes text and then creates a
#dictionary of chords and a dictionary of the notes.
def process_files():
    file1 = open("chords.txt")
    lines = file1.readlines()
    chords = {}
    for line in lines:
        key = line.split()
        chords[key[0]] = key[1:]
        
    file2 = open("notes.txt")
    lines2 = file2.readlines()
    frets = {}
    for line in lines2:
        key2 = line.split()
        frets[key2[0]] = key2[1:]

    return chords, frets

#This function generates a random chord progression based on the user input.
#The function then returns a list of the chord progression
def create_chord_progression(desired_key, num_unique_chords,
                            chord_dict):
    chord_progression = []
    while len(chord_progression) < num_unique_chords:
        rand_num = random.randint(0, len(chord_dict[desired_key]) - 1)
        chord = chord_dict[desired_key][rand_num]
        chord_prog_string = ''
        if chord not in chord_progression:
            chord_progression.append(chord)

        for i in range(len(chord_progression)):
            chord_prog_string += (chord_progression[i] + " ")

    print("Chord Progression: " + chord_prog_string)
    return chord_progression

#This function generates 24 random notes from the desired key.
def solo_note_generator(desired_key, fret_dict):
    solo_notes = []
    while len(solo_notes) < NUM_SOLO_NOTES:
        rand_num = random.randint(0, len(fret_dict[desired_key]) - 1)
        notes = fret_dict[desired_key][rand_num]
        solo_notes.append(notes)
    return solo_notes

#This function creates a returns a list of lists that when printed,
#represents a music staff with the generated notes appearing on it.
def create_solo_list(STRINGS, solo_notes):
    solo_list = []
    for i in range(len(STRINGS)):
        temp = []
        temp.append(STRINGS[i])
        temp.append("|")
        solo_list.append(temp)

    for i in range(NUM_SOLO_NOTES):
        for j in range(len(STRINGS)):
            if solo_notes[i][0] == solo_list[j][0]:
                solo_list[j].append(solo_notes[i][1])
                solo_list[j].append("-")
                solo_list[j].append("-")
            else:
                solo_list[j].append("-")
                solo_list[j].append("-")
                solo_list[j].append("-")
                   
    return solo_list

#This function prints the list of lists that provides the visual representation
#of the staff
def draw_staff(solo_list):
    
    for i in range(len(solo_list)):
        for j in range(len(solo_list[i])):
            print(solo_list[i][j], end="")
        print()
        
    
                   
main()
