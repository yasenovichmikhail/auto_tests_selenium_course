import turtle

def triangle(side):
    for i in range(3):
        turtle.forward(side)
        turtle.left(120)

side = 200

triangle(side)