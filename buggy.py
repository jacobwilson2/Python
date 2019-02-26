#Jacob Wilson
#Allison Obourn
#csc110_1L
#project_9
#part_2

# This is the code that you will need to debug, test and
# fix the style of for Project 9 Part B.

# This program reads in data about the Scottish Independence
# referendum and outputs data about each shire's votes
# It then outputs the result of the referendum and
# What percentage voted for independence in each shire

def main():
    file = open("voting.txt")
    lines = file.readlines()
    for m in range(0, len(lines), 2):
        shire_name = lines[m].strip()
        shire_yes_votes = 0
        shire_votes = 0

        for v in range(0, len(lines[m+1])):
            if lines[m+1][v].lower() == 'n':
                total_voters += 1
                shire_votes += 1
            elif lines[m+1][v].lower() == 'y':
                total_voters += 1
                shire_votes += 1
                shire_yes_votes += 1
                total_yes += 1
            elif lines[m+1][v].lower() == "a":
                shire_votes += 1
                total_voters += 1

        print("percentage:" + (str(count/countAl)))
    
    print("Overall there were ", (count/countAll),"  yes votes")

main()
      


main()
