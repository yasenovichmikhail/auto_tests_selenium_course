import turtle
window = turtle.Screen()

def get_line(side):
    for i in range(1):
        turtle.left(90)
        turtle.forward(side)

side = 5

def get_labyrinth():
    counter = side
    get_line(side)
    for j in range(50):
        counter += 5
        get_line(counter)

get_labyrinth()

window.exitonclick()