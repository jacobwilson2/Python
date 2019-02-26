#Jacob Wilson
#Allison Obourn
#csc110_1L
#project 12

#This function prints an intro and gives the user instructions on how
#to use the program.
def intro():
    print("Welcome to the CSC110 Book Recommender. Type the word in the")
    print("left column to do the action on the right.")
    print("recommend : recommend books for a particular user")
    print("averages    : output the average ratings of all books in the system")
    print("quit        : exit the program")

#This function creates a list of each book in the input file
def create_booklist(lines):
    book_list = set()
    for i in range(0, len(lines), 3):
        book_list.add(lines[i+1].strip('\n '))
    book_list = list(book_list)
    
    return book_list

#This function creates a dictionary mapping each person to their ratings
#for each book
def create_dictionary(lines, book_list):
    people = set()
    rating_dict = {}
    for i in range(0, len(lines), 3):
        people.add(lines[i].strip('\n '))
    people = list(people)
    
    for person in people:
        rating_dict[person] = [0] * len(book_list)
    
    for i in range(1, len(lines), 3):
        book_index = book_list.index(lines[i].strip('\n '))
        rating_dict[lines[i-1].strip('\n ')][book_index] = int(lines[i+1].strip('\n '))
                            
    return rating_dict

#This function calculates the average rating of each book
def calculate_averages(book_list, rating_dict):
    avgs = []
    for i in range(len(book_list)):
        rating_sum = 0
        count = 0
        for key in rating_dict.keys():
            if rating_dict[key][i] != 0:
                count += 1
            rating_sum += rating_dict[key][i]
            
    
        average = rating_sum / count
        average_tuple = (str(book_list[i]), average)
        avgs.append(average_tuple)
        avgs.sort(reverse=True)
        
        sorted_list = sorted(avgs, key=lambda tup: tup[1])[::-1]
    average_tuple = ''
    for element in sorted_list:
        average_tuple += element[0] + " " + str(element[1]) + "\n"
    return average_tuple

#This function recommends books to a user based on their ratings of
#other books.
def recommendations(book_list, rating_dict, average_tuple):
    user = input("user? ")
    similarity = []
    if user not in rating_dict.keys(): #returns average ratings if the user is not found in dict
        print(average_tuple)
    for person in rating_dict: #calculates dot sum
        if person != user:
           dot_sum = 0
           for i in range(len(rating_dict[person])):
               dot_sum += (rating_dict[person][i] * rating_dict[user][i])
            
           similarity_tuple = (dot_sum, person) #makes tuple of rating and person
           similarity.append(similarity_tuple) 
           similarity.sort(reverse=True) #sorts ratings
   
    name1 = similarity[0] 
    name2 = similarity[1]
    name3 = similarity[2]
    total_sum = 0
    tuple_list = []
  
    for i in range(len(book_list)): #finds the average rating of each book for the three most similar people
        avg_rating = 0
        count = 0
        total_sum = (rating_dict[name1[1]][i] + rating_dict[name2[1]][i] +
                     rating_dict[name3[1]][i])
              
        if rating_dict[name1[1]][i] != 0:
            count += 1
        if rating_dict[name2[1]][i] != 0:
            count += 1
        if rating_dict[name3[1]][i] != 0:
            count += 1
        if total_sum == 0 and count == 0:
            avg_rating = 0
        elif total_sum != 0 or count != 0:
            avg_rating = total_sum / count
        
        rating_tuple = (book_list[i], avg_rating)
        tuple_list.append(rating_tuple)
    tuple_list.sort(reverse=True)
  
    for item in tuple_list:
        if item[1] <= 0.1:
            tuple_list.remove(item)
            
    sorted_tuple = sorted(tuple_list, key=lambda tup: tup[1])[::-1] #sorts tuple
    for item in sorted_tuple:
        if item[1] <= 0:
            sorted_tuple.remove(item)
            
    recommendations = ''
    for element in sorted_tuple:
        recommendations += element[0] + " " + str(element[1]) + "\n"
    print(recommendations)

#This program reads a file of users and their book ratings. The user can then
#interact with the program and choose to either see the average ratings of the
#books, or get book recommendations for books based on previous book ratings
def main():
    intro()
    task = 0
    while task != 'quit': 
        task = input("next task? ")
        file = open("ratings-small.txt")
        lines = file.readlines()
        book_list = create_booklist(lines)
        rating_dict = create_dictionary(lines, book_list)
        average_tuple = calculate_averages(book_list, rating_dict)
  
        if task == 'averages':
            print(average_tuple)
        if task == 'recommend':
            recommendations(book_list, rating_dict, average_tuple)
        
    return

main()
