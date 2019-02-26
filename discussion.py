#def pyramid(n, char):
#    for i in range(1, n + 1):
#        print(" " * (-i + 4) + "*" * (i * 2 - 1))
    
#pyramid(4, "-")

#def count_by(n, z):
#    for i in range(0, z, n):
#        print(i, end= " ")

#count_by(10, 93)

#def print_stars():
#    stars= int(input("How many stars?"))
#    print("*" * stars)

#print_stars()

#def box():
#    Width= int(input("Width?"))
#    print()
#    Height= int(input("Height?"))
#    print()
#    print("The area is " + str(Width * Height))

#box()
    
#def the_who():
#    for i in range(1, 6):
#        a= input("Word")
#        print(a * i)
    
#the_who()

#from DrawingPanel import *

#def main(height):
#    height= int()
#    panel = DrawingPanel(250, 250, background= "red")
#    for i in range(0, 6):
#        panel.draw_oval((0 + 50 * i), (0 + 1 * height), 100, 100)

#main(100)


#def main():
#    a = 4
#    b = 7
#    c = -2
#
#    mystery(c, 3, a)
#    mystery(a + b, b + c, c + a)

#def mystery(c, a, b):
#    print(str(b), " + " + str(c), " = ", str(a))

#main()

#from DrawingPanel import*

#def main(x, y):
#    panel = DrawingPanel(x, y, background= "cyan")
#    panel.draw_line(50, 50, 150, 150, "red")

#    for i in range(1, 6):
#        panel.draw_rect(50, 50, 20 * i, 20 * i, "red")

from DrawingPanel import*

def main():
    panel = DrawingPanel(600, 200, background= "yellow")
    for i in range(1, 20):
        panel.draw_line(i * 20, i * 10, 600 - i * 20, i * 10)

main()
    
