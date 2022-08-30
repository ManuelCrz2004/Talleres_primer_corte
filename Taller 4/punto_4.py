# Hacer una función con un espiral del cuadrados, esta debe tener 5 cuadrados

import turtle


def cuadrado(t, size):
    
    for i in range(4):
        t.fd(size)
        t.rt(360 / 4)

def spiral(t, size):
    for i in [1, 2, 4, 8, 16, 32]:
        cuadrado(t, size / i)
        t.back(size/(2 * i))
        t.lt(90)
        

wn = turtle.Screen()
mariana = turtle.Turtle()

spiral(mariana, 200)

wn.mainloop()