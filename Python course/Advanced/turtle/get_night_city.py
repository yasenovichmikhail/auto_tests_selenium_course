import turtle as t
from random import *

t.clear()
t.hideturtle()
t.Screen().bgcolor('midnightblue')
t.Screen().colormode(255)
t.speed(0)

t.penup()
t.goto(230, 250)
t.dot(100,'yellow')
t.goto(210, 250)
t.dot(100, 'midnightblue')

for _ in range(100):
    t.goto(randint(-350, 350), randint(-350, 350))
    t.dot(randint(2, 10), 'yellow')
    

for _ in range(33):
    t.penup()
    height = randrange(80, 400)
    t.goto(randint(-350, 380), -350 + height)
    t.pendown()
    t.begin_fill()
    t.fillcolor(randrange(254), randrange(254), randrange(254))
    t.right(90)
    
    for _ in range(2):
        t.forward(height)
        t.right(90)
        t.forward(70)
        t.right(90)
    t.end_fill()
    t.left(90)    
    
    t.begin_fill()
    for _ in range(2):
        t.left(45)
        t.forward(40)
        t.left(135)
        t.forward(70)
    t.end_fill()    
    t.left(45)
    
    t.begin_fill()
    for _ in range(2):
        t.forward(40)
        t.right(135)
        t.forward(height)
        t.right(45)
    t.end_fill()
    
    t.left(135)
    
    color = ('yellow', 'darkslateblue')
    position = (t.xcor() - 10, t.ycor() - 10)
    t.shape('square')
    t.shapesize(0.6)
    
    for i in range(0, height - 34, 17):
        t.penup()
        t.goto(position[0], position[1] - i)
        for _ in range(4):
            t.fillcolor(choice(color))          
            t.stamp()
            t.penup()
            t.forward(17)
    t.left(180)