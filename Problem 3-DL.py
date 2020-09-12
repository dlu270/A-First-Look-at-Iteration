#Daniel Lu
#08/08/2020

#This program asks the user for the number of sides of a shape, the length of sides and the color.  It then draws the shape and colors it.

import turtle
wn = turtle.Screen()
bob = turtle.Turtle()

sides = input ("What are the number of sides of the polygon?: ")
length = input ("What is the length of the sides of the polygon?: ")
line_color = input ("What is the line color of the polygon?: ")
fill_color = input ("What is the fill color of the polygon?: ")

bob.color(line_color)
bob.fillcolor(fill_color)
bob.begin_fill()

for i in range (int(sides)):
    bob.forward (int(length))
    bob.left (int(360) / int(sides))

bob.end_fill()
