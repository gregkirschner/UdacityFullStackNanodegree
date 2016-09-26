import turtle, random

t = turtle.Turtle()
t.speed(9)
window = turtle.Screen()

#Random background color
window.bgcolor(random.random(),random.random(),random.random())

#Stem
t.color = (random.random(),random.random(),random.random())
t.lt(90)
t.forward(150)

def triangle(size):
	for i in range(3):
		t.forward(size)
		t.rt(240)

def flower(size):
	for i in range(36):
		triangle(size)
		t.rt(10)


flower(50)

window.exitonclick()
