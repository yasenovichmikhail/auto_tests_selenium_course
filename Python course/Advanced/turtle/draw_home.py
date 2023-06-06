import turtle
from random import randrange
window = turtle.Screen()

def square(side):
    turtle.fillcolor('blue')
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-20, 100)
    turtle.pendown()
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.goto(50, 200)
    turtle.goto(120, 100)
    turtle.goto(-20, 100)
    turtle.end_fill()

side = 100

square(side)

window.exitonclick()