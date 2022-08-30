# Hacer una estrella de david como se muestra en la imagen

import turtle

def triangulo(t, sz):
    for i in range(3):
        t.fd(sz)
        t.lt(360 / 3)
    
def estrella(t, sz):
    t.lt(60)
    triangulo(t, sz)
    t.lt(60)
    t.fd(sz/3)
    t.lt(240)
    t.bk(sz/3)
    triangulo(t, sz)
    
wn = turtle.Screen()
mariana = turtle.Turtle()

estrella(mariana, 100)

wn.mainloop()