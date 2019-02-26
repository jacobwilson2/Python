#Jacob Wilson
#csc110_1L
#project 4
#doodle

from DrawingPanel import*

def main():
    panel = DrawingPanel(500, 500, background= "skyblue")

    for i in range(60):
        ball1x = 100
        ball2x = 400
        ball1y = 0
        ball2y = 0
        disp = displacement(25, 9.81, i)
        panel.fill_oval(ball1x, (ball1y + int(disp)), 10, 10, "black")
        panel.fill_oval(ball2x, (ball2y + int(disp)), 10, 10, "red")
        

        panel.sleep(1000)
        panel.fill_rect(0, 0, 600, 600, "skyblue")
        panel.fill_oval(50, 385, 100, 60, "black")
        panel.fill_oval(350, 385, 100, 60, "red")

def displacement(vO, a, t):
    d = vO * t + 0.5 * a * (t**2)
    return d

main()
