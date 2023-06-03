import turtle

def get_line_clock(n, x):
  
  x = 360 / n
  for j in range(n):
     turtle.penup()
     turtle.forward(100)
     turtle.pendown()
     turtle.forward(10)
     turtle.penup()
     turtle.backward(110)
     turtle.left(x)

def get_turtle_clock(n, x):
  turtle.shape('turtle')
  turtle.stamp()

  for i in range(n):
      turtle.penup()
      turtle.forward(130)
      turtle.pendown()
      turtle.stamp()
      turtle.penup()
      turtle.backward(130)
      turtle.left(x)

n = 12
x = 360 / n

get_line_clock(n, x)
get_turtle_clock(n, x)

