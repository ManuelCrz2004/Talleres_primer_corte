# Hacer la figura mostrada en el image, la cual consiste en 4 triangulos y 1 cuadrado

import turtle

def cuadrado(t, sz):
    for i in range(4):
        t.fd(sz)
        t.rt(360 / 4)

def triangulos(op1, op2, op3, sz, t):
    if op1 == "arriba" and op2 == "hipotenusa":
        t.fd(sz)
        t.lt(90 + 90/2)
        
        

def figura(t, sz):
    t.penup()
    t.goto(-sz/2, sz/2)
    t.pendown()
    cuadrado(t, sz)
    t.lt(90)

wn = turtle.Screen()
mariana = turtle.Turtle()

figura(mariana, 100)

wn.mainloop()