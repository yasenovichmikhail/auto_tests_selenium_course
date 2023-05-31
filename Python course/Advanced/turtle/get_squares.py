import turtle
window = turtle.Screen()

def square(side):
    for i in range(3):
        turtle.left(20)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)

side = 200

square(side)

window.exitonclick()