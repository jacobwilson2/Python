#Jacob Wilson
#Project2
#csc110_1L

#PartA
#Cat

def bar():
    print("+-----------------------+")

def ears():
    print("   ^              ^     ")
    print(" /   \\__________/   \\  ")

def eyes():
    print("|       ^       ^       |")

def face():
    print("|                       |")
    print("|   \\               /   |")
    print("|    --------------     |")

def body():
    for i in range(1,5):
        print(" " * 11 + "|" + " " * 11)

def legs():
    print(" " * 10 + "/" + " " + "\\")




    
def main():
    ears()
    bar()
    eyes()
    face()
    bar()
    body()
    legs()

main()
