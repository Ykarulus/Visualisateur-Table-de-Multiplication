from tkinter import *
import math

def PurcentageToCoordinatesX(Purcentage):
    return math.cos(360*(Purcentage)/100*math.pi/180)* 480 + 500
def PurcentageToCoordinatesY(Purcentage):
    return math.sin(360*(Purcentage)/100*math.pi/180)*480 + 500
def create_circle(x, y, r, canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1)
def line_creation(PurcentageCircle1, PurcentageCircle2 ):
    MyCanvas.create_line(
        PurcentageToCoordinatesX(PurcentageCircle1),
        PurcentageToCoordinatesY(PurcentageCircle1),
        PurcentageToCoordinatesX(PurcentageCircle2),
        PurcentageToCoordinatesY(PurcentageCircle2),
        fill="black")


Modularity= int(input("Entrer la base modulaire : "))
Table = float(input("Entrer la table : "))

MyWindow = Tk()

MyCanvas = Canvas(MyWindow, width=1000, height=1000, bg='ivory')

create_circle(500, 500 , 480, MyCanvas)




for i in range(Modularity):

    a = 100/Modularity
    b=i*a
    line_creation(b, b*Table)


MyCanvas.pack()

MyWindow.mainloop()

