# Codigo con el fin de realizar cuadrados, con el cuadrante inferior izquierdo relleno

import turtle
import math

def hacer_cuadrado(t, sz):
    for i in range(4):
        t.fd(sz)
        t.lt(360 / 4)

def cuadrado_grande(t, sz):
    hacer_cuadrado(t, sz)

wn = turtle.Screen()
mariana = turtle.Turtle()

turtle.begin_fill()
cuadrado_grande(mariana, 40)
turtle.end_fill()


wn.mainloop()