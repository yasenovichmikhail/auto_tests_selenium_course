import turtle

def get_color_labyrinth():
    colors=['red', 'blue', 'yellow', 'green', 'purple', 'orange']
    s=10
    n=150
    for i in range(8):
        for j in colors:
            turtle.pensize(s)
            turtle.pencolor(j)
            turtle.forward(n)
            turtle.right(45)
            n-=3
        s-=2

get_color_labyrinth()