from turtle import Screen, Turtle
from math import sqrt

x1 = 45
y1 = int(input('Introduce y1: '))
x2 = int(input('Introduce x2: '))
y2 = int(input('Introduce y2: '))

pantalla = Screen ()
DIMX = 400
DIMY = 200

pantalla.setup (DIMX + 25, DIMY + 25)
pantalla.screensize(DIMX, DIMY)


tortuga = Turtle ()

XY = sqrt((x2 - x1)**2 + (y2 - y1)**2)
tortuga.write(XY)

#Código

tortuga.penup ()
tortuga.goto (x1, x2)
tortuga.pendown ()
tortuga.goto (y1, y2)

print('La longitud del segmento intrducido es: ', XY, )
pantalla.exitonclick()
