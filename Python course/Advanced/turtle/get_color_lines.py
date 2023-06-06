import turtle
window = turtle.Screen()

def get_color_lone():
    for i in range(-200, 200, 40):
        turtle.dot(10, 'red')
        turtle.pencolor('green')
        turtle.goto(i, -200)
        turtle.dot(10, 'blue')
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()

get_color_lone()

window.exitonclick()