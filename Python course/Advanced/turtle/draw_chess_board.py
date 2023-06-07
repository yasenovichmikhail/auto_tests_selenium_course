import turtle
window = turtle.Screen()

turtle.hideturtle()
turtle.speed(0)
points = [(0, 0), (50, -50), (100, 0), (150, -50), (200, 0), (0, -100),
 (100, -100), (200, -100), (50, -150), (150, -150), (0, -200), (100, -200), (200, -200)]

def get_black_square():
    turtle.begin_fill()
    for i in range(4):
        turtle.fillcolor('black')
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()

def get_points():
    for k in range(len(points)):
        turtle.goto(points[k])
        turtle.pendown()
        get_black_square()

def get_big_square():
    for i in range(4):
        turtle.forward(250)
        turtle.right(90)

get_big_square()
get_points()

window.exitonclick()