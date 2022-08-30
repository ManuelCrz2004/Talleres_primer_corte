# Codigo con el fin de realizar cuadrados, con el cuadrante inferior izquierdo relleno

import turtle
import math

def hacer_cuadrado(t, sz):
    for i in range(4):
        t.fd(sz)
        t.lt(360 / 4)

def cuadrado_pintado(t, sz):
    turtle.color("black", "black")
    turtle.begin_fill()
    for i in range(4):
        t.fd(sz)
        t.lt(360 / 4)
        turtle.end_fill()

wn = turtle.Screen()
mariana = turtle.Turtle()

cuadrado_pintado(mariana, 60)


wn.mainloop()