#JacobWilson
#AllisonObourn
#Csc110_1L
#Project5


#This program accepts a user's input of their coursework for the semester.
#The program then computes and reports the user's overall course grade.
def main():
    intro()
    print()
    calculate_grade()

    
#This function briefly explains the what the program is supposed to do    
def intro():
    print("This program reads exam/homework scores")
    print("and reports your overall course grade.")

    
#This function accepts parameters to determine whether the test
#is a midterm or final.
#This function ultimately computes the weighted score of each test
def bigTest(x, n):
    if(x == "m"):
        print("Midterm " + str(n) + ":")
    else:
        print("Final:")
    
    weight = int(input("Weight  (0-100)? "))
    score = int(input("Score earned? "))
    shift = int(input("Were scores shifted  (1=yes, 2=no)? "))
    if shift == 1:
        shift_value = int(input("Shift amount? "))
    else:
        shift_value = 0
        
    result = score + shift_value
    if result > 100:
        result = 100
    total_points = int(100)
    weight_score = (result / total_points) * weight
    print("Total points = " + str(result) + " / " + str(total_points))
    print("Weighted score = " + str(round(weight_score, 1)) + " / "
          + str(weight))
    return(weight_score)

#This function computes the user's weighted score for homework
def homework():
    print("Homework:")
    weight = int(input("Weight  (0-100)? "))
    num = int(input("Number of assignments? "))
    total_score = 0
    max_score = 0
    for i in range(1, num + 1):
        score = int(input("Assignment " + str(i) + " score? "))
        points = int(input("Assignment " + str(i) + " max? "))
        total_score += score
        max_score += points
    
        
    sections = int(input("How many sections did you attend? "))
    sections *= 3
    if sections > 34:
        sections = 34
    total_score += sections
    max_score += 34
    if total_score > max_score:
        total_score = max_score
    weight_score = (total_score / max_score) * weight
    print("Section points = " + str(sections) + " / " + str(34))
    print("Total points = " + str(total_score) + " / " + str(max_score))
    print("Weighted score = " + str(round(weight_score, 1))
          + " / " + str(weight))
    return(weight_score)

#This function accepts parameters to determine whether to compute the
#homework or quiz weighted scores.
def quizzes_and_daily(x):
    if x == "q":
        print("Quizzes:")
    else:
        print("Daily homework:")
        
    weight = int(input("Weight  (0-100)? "))
    points_earned = int(input("Total points earned? "))
    points_possible = int(input("Total points possible? "))
    if points_earned > points_possible:
        points_earned = points_possible
    weight_score = (points_earned / points_possible) * weight
    print("Total points = " + str(points_earned) + " / "
          + str(points_possible))
    print("Weighted score = " + str(round(weight_score, 1))
          + " / " + str(weight))
    return(weight_score)    

#This function sums up the weighted scores for all the coursework
#throughout the semester. The function then gives the user a
#letter grade based on the cummulative sum.
def calculate_grade():
    WeightedMidterm1Score = bigTest("m",1)
    print()
    WeightedMidterm2Score = bigTest("m",2)
    print()
    WeightedFinalScore = bigTest("f", 0)
    print()
    WeightedHomeworkScore = homework()
    print()
    WeightedQuizScore = quizzes_and_daily("q")
    print()
    WeightedDailyProblemsScore = quizzes_and_daily("d")
    print()

    grade = (WeightedMidterm1Score + WeightedMidterm2Score
             + WeightedFinalScore + WeightedHomeworkScore
             + WeightedQuizScore + WeightedDailyProblemsScore)

    print("Overall percentage = " + str(round(grade, 1)))
    
    if grade >= 90:
        print("Your grade will be at least: A")
        print("GREAT JOB!")

    elif grade >= 80:
        print("Your grade will be at least: B")
        print("Nice work")

    elif grade >= 70:
        print("Your grade will be at least: C")
        print("You win some, you lose some")

    elif grade >= 60:
        print("Your grade will be at least: D")
        print("'D's still get degrees")

    else:
        print("Your grade will be at least: F")
        print("McDonalds is hiring!")
            
main()
