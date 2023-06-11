import turtle

def get_turtle_web(n):
  x = 360 / n
  turtle.shape('turtle')
  turtle.stamp()
  for i in range(n):
      turtle.penup()
      turtle.forward(100)
      turtle.pendown()
      turtle.stamp()
      turtle.penup()
      turtle.backward(100)
      turtle.left(x)

n = 10

get_turtle_web(n)