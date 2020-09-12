#Daniel Lu
#08/08/2020

#This program draws a yellow star.

import turtle
def star(size, color):
    angle = 144
    turtle.fillcolor(color)
    turtle.begin_fill()

    for side in range(5):
        turtle.forward(size)
        turtle.right(angle)
        turtle.forward(size)
        turtle.right(72 - angle)
    turtle.end_fill()
    return

star(150, "yellow")