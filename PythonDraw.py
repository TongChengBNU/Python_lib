# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 19:50:56 2020

@author: 75934
"""
# PythonDraw.py

# turtle is a standard library
import turtle

# generate a canvas
# turtle.setup(width, height, startx, starty)
turtle.setup(650, 350, 200, 200)

# turtle.colormode(mode) 
# mode: 1.0, 255

# turtle.goto(x, y)

# raise up turtle, no stroke on canvas
turtle.penup()

# forward
turtle.fd(-250)

# backward
# turtle.bk(distance)

# put down turtle, stroke appears on canvas
turtle.pendown()

# turtle.width(width)
turtle.pensize(25)

# turtle.pencolor(color)
# color: str, rgb-float, rgb-tuple_float
turtle.pencolor("purple")

# change direction (set head)
# turtle.seth(angle)
turtle.seth(-40)
# turtle.left(angle)
# turtle.right(angle)

for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()

