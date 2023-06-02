import turtle
window = turtle.Screen()

def triangle_left():
    for i in range(3):
        turtle.forward(200)
        turtle.left(120)

def triangle_right():
    for i in range(3):
        turtle.forward(200)
        turtle.right(120)

circle = [(100, -100), (0, 70), (200, 70)]
triangle_left()

def get_circle():
    for j in circle:
        turtle.penup()
        turtle.goto(j)
        turtle.pendown()
        turtle.fillcolor('black')
        turtle.begin_fill()
        turtle.circle(30)
        turtle.end_fill()

get_circle()

turtle.penup()
turtle.goto(0, 100)
turtle.pendown()

turtle.fillcolor('white')
turtle.begin_fill()
triangle_right()
turtle.end_fill()

window.exitonclick()