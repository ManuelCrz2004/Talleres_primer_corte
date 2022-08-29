# programa para dibujar polinomios regular, con excepcion tess

import turtle

def draw_poly(t, n ,sz):
    for i in range(n):
        t.fd(sz)
        t.lt(360 / n)

wn = turtle.Screen()
mariana = turtle.Turtle()

draw_poly(mariana, 8, 50)

wn.mainloop()