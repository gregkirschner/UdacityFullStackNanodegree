import turtle

myTurtle = turtle.Turtle()
myTurtle.shape('turtle')
myTurtle.speed(8)

"""
A side exercise was used to draw a circle & triangle.
##myCircle = turtle.Turtle()
##myCircle.shape('arrow')
##myCircle.speed(6)
##
##myTriangle = turtle.Turtle()
##myTriangle.shape('circle')
##myTriangle.speed(7)
"""

window = turtle.Screen()
window.bgcolor('#5500AA')

def draw_square():
        sides = 0
        while sides < 4:
                myTurtle.forward(100)
                myTurtle.lt(90)
                sides += 1
        myTurtle.fill()

def draw_circle():
        myCircle.circle(50)

def draw_triangle():
        tri_sides = 0
        while tri_sides < 3:
                myTriangle.forward(75)
                myTriangle.rt(240)
                tri_sides += 1

def next_square():
        myTurtle.lt(20)

total_squares = 19

for each in range (1, total_squares):
    if each % 2 == 0:
        myTurtle.fillcolor('#FF0033')
        myTurtle.color('#FF00FF')
    else:
        myTurtle.fillcolor('#0033FF')
        myTurtle.color('#00FF00')
    draw_square()
    next_square()

window.exitonclick()

