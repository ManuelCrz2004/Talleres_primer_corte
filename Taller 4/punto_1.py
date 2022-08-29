# Programa el cual dibuja una cruz, usando el modulo turtle

import turtle

def dibujar_cruz(t, s1, l, s2):
    t.fd(l)
    t.lt(360/4)
    t.fd(s2)

    for i in range(3):
        t.rt(360/4)
        t.fd(s1)
        t.lt(360/4)
        t.fd(l)
        t.lt(360/4)
        t.fd(s2)
    
    t.rt(360/4)
    t.fd(s2)

wn = turtle.Screen()
mariana = turtle.Turtle()

dibujar_cruz(mariana, 40, 50, 40)

wn.mainloop()