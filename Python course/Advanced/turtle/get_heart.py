import turtle, math

turtle.up()
def dart():
    turtle.goto(0, -50)
    turtle.down()
    turtle.pensize(5)
    turtle.left(45)
    turtle.forward(150)
    turtle.left(180)
    turtle.forward(50)
    turtle.left(180)
    for _ in range(5):
        x, y = turtle.pos()
        turtle.left(45)
        turtle.forward(15)
        turtle.goto(x, y)
        turtle.right(90)
        turtle.forward(15)
        turtle.goto(x, y)
        turtle.left(45)
        turtle.forward(10)
    turtle.up()
    turtle.goto(-56, -106)
    turtle.left(180)
    turtle.down()
    turtle.forward(60)
    turtle.shape('arrow')
    turtle.stamp()
        
    
def heart():
  turtle.fillcolor('red')
  turtle.begin_fill()
  for t in range(630):
    t *= 0.01
    x = 128*math.sin(t)**3
    y = 8*(13*math.cos(t)-5*math.cos(2*t)-2*math.cos(3*t)-math.cos(4*t) - 5)
    turtle.goto(x, y)
  turtle.end_fill()
        
heart()
dart()