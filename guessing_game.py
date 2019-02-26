#Jacob Wilson
#Csc110_1L
#Allison Obourn
#project 6

#This program chooses a random number and then allows the user to keep
#guessing until they guess the correct number. After the correct number
#has been identified, the program prompts the user to play again.
#If the user says no or uses any other word that starts with an "n",
#The program jumps to the user's guessing statistics.
def main():
    haiku()
    total_games, total_count, best_game, average = play_again()
    statistics(total_games, total_count, best_game, average)
    
#This function prints a haiku that relates to numbers.
def haiku():
    print("Number on number")
    print("I'm thinking of a number")
    print("Can you guess it?")
    print()

#This function plays one guessing game and returns the amount of guesses
#it took the user to guess the correct number.
import random
def play_game():
    count = 1
    guess = 0
    print("I'm thinking of a number between 1 and 100...")
    num = int(random.randint(1, 100))
    
    while num != guess:
        guess = int(input("Your guess? "))
                   
        if num > guess:
            print("It's higher.")
            count += 1

        elif num < guess:
            print("It's lower.")
            count += 1

        else:
            if count == 1:
                print("You got it right in 1 guess!")
            else:
                print("You got it right in " + str(count) + " guesses!")
                break

    return count

#This function contains a loop that allows the user to keep playing until
#they no longer wish to play. This fuction also keeps track of statistics
#as the games are played and then returns the statistics to be used
#in the statistic function.
def play_again():
    total_count = 0
    total_games = 0
    play_again = "yes"
    best_game = 1000
    
    while play_again[0].lower() == "y":
        total_games += 1
        count = play_game()
        if count < best_game:
            best_game = count
        total_count += count
        average = total_count / total_games
        average = round(average, 1)
        play_again = str(input("Do you want to play again? "))
        print()

    return total_games, total_count, best_game, average


#This function reports the user's guessing game statistics.        
def statistics(total_games, total_count, best_game, average):
    print("Overall results:")
    print("Total games   = " + str(total_games))
    print("total guesses = " + str(total_count))
    print("Guesses/game  = " + str(average))
    print("Best game     = " + str(best_game))
    
                
main()

    
          
