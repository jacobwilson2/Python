#Jacob Wilson
#Csc110_1L
#Project 7

from DrawingPanel import*

def main():
    intro()
    eligible_voters, search_state, dem_list, rep_list = process_state()
    draw_graph(eligible_voters, search_state, dem_list, rep_list)
                        
def intro():
    print("This program allows you to search through")
    print("data about congressional voting districts")
    print("and determine whether a particular state is")
    print("gerrymandered")
    print()

def process_state():
    search_state = input("Which state do you want to look up? ")
    search_state = search_state.capitalize()
    file = open("districts.txt")
    lines = file.readlines()

    for line in lines:
        if search_state == line.split(",")[0]:
            parts = line.split(",")
            dist = 0
            wasted_dem = 0
            wasted_rep = 0
            dem_list = []
            rep_list = []

            for i in range(1, len(parts), 3):
                dem_votes = int(parts[i + 1])
                rep_votes = int(parts[i + 2])
                dem_list.append(dem_votes)
                rep_list.append(rep_votes)
                total_votes = (dem_votes + rep_votes)                      
                if dem_votes > rep_votes:
                    wasted_rep += rep_votes
                    wasted_dem += dem_votes - ((total_votes // 2) +1)

                else:
                    wasted_dem += dem_votes
                    wasted_rep += rep_votes - ((total_votes // 2)+1)

    file1 = open("eligible_voters.txt")
    lines = file1.readlines()
    for line in lines:
        if search_state == line.split(",")[0]:
            parts1 = line.split(",")
            eligible_voters = parts1[1].strip()
            

    print("Total Wasted Democratic votes: " + str(wasted_dem))
    print("Total Wasted Democratic votes: " + str(wasted_rep))
    print(str(eligible_voters) + " eligible voters")

    return eligible_voters, search_state, dem_list, rep_list
    

def draw_graph(eligible_voters, search_state, dem_list, rep_list):
    
    panel = DrawingPanel(500, 500)
    panel.draw_line(0, 20, 500, 20)
    panel.draw_line(250, 0, 250, 500)
    panel.draw_string((search_state), 0, 0)
    panel.draw_string(eligible_voters + " eligible voters", 380, 0)
    
    for i in range(0, len(dem_list)):
        dem_width = dem_list[i] / (dem_list[i] + rep_list[i]) * 500
        rep_width = rep_list[i] / (dem_list[i] + rep_list[i]) * 500
        panel.fill_rect(0, (i + 1) * 25, dem_width, 20, "blue")
        panel.fill_rect(500, (i + 1) * 25, -rep_width, 20, "red")
            
main()
