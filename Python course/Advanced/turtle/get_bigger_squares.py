import turtle
window = turtle.Screen()

def square(side):
    for i in range(1):
        turtle.setheading(180)
        turtle.forward(side)
        turtle.right(90)
        turtle.forward(side)
        turtle.right(90)
        turtle.forward(side)
        turtle.right(90)
        turtle.forward(side)
        turtle.right(90)

side = 10

def bigger_square():
    square(side)
    counter = side
    for j in range(30):
        counter += 5
        square(counter)

bigger_square()

window.exitonclick()