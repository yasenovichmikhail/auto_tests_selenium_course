import turtle
window = turtle.Screen()

colors = ['blue', 'black', 'red', 'yellow', 'green']

lst = [(0, 0), (200, 0), (400, 0), (100, -150), (300, -150)]

def get_ring(x, y):
    turtle.pensize(7)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(100)
    turtle.penup()

def get_olympic_rings():
    for i in range(len(lst)):
        turtle.pencolor(colors[i])
        get_ring(lst[i][0], lst[i][1])

get_olympic_rings()

window.exitonclick()