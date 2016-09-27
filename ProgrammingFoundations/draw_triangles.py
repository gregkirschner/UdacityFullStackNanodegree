import turtle, random

t = turtle.Turtle()
t.speed(8)
window = turtle.Screen()

def one_triangle(s):
    t.fill(True)

    #Random (mostly) colors to fill in the triangles
    r = int( random.random() * 255 // 1)
    hex_r = hex(r)[2:].upper()
    g = int( random.random() * 255 // 1)
    hex_g = hex(g)[2:].upper()
    b = int( random.random() * 255 // 1)
    hex_b = hex(b)[2:].upper()
    hex_color = '#'+hex_r+hex_g+hex_b
    if len(hex_color) == 4:
        hex_color += 'F0F'
    if len(hex_color) == 5:
        hex_color += 'FF'
    if len(hex_color) == 6:
        hex_color += '0'
    t.fillcolor(hex_color)

    #Draw triangle
    for i in range(3):
        t.forward(s)
        t.rt(240)
    t.fill(False)

def three_triangles(s):
    init_pos = t.pos()
    low_rt = (s + init_pos[0],init_pos[1])

    #First triangle (top)
    one_triangle(s)

    #Setup for second triangle 
    t.goto(low_rt)
    t.lt(240)

    #Second triangle (lower left)
    one_triangle(s)

    #Setup for third triangle 
    t.goto(init_pos)

    #Third triangle (lower right)
    one_triangle(s)

    t.forward(s)

def nine_triangles(s):
    #First set of three triangles (top)
    three_triangles(s)

    #Setup for second three
    t.forward(s)
    t.rt(240)
    
    #Second set of three triangles (lower left)
    three_triangles(s)

    #Setup for third set of three triangles
    t.rt(240)
    t.forward(s*4)
    t.rt(240)
    t.forward(s)
    t.lt(240)
    t.back(s)

    #Third set of three triangles  (lower right)
    three_triangles(s)

def twenty_seven_triangles(s):
    #First set of nine triangles (top)
    nine_triangles(s)

    #Setup for second set of nine triangles 
    t.rt(240)
    t.back(s*2)
    t.lt(240)
    t.forward(s)
    t.rt(240)

    #Second set of nine triangles (lower left)
    nine_triangles(s)

    #Setup for third set of nine triangles
    t.rt(240)
    t.forward(s*6)
    t.rt(240)
    t.forward(s*3)
    t.lt(240)
    t.back(s)

    #Third set of nine triangles
    nine_triangles(s)
    
twenty_seven_triangles(30)

window.exitonclick()
