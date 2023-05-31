import turtle

def rectangle(width, height):
  turtle.forward(width)
  turtle.left(90)
  turtle.forward(height)
  turtle.left(90)
  turtle.forward(width)
  turtle.left(90)
  turtle.forward(height)
  
width = 200
height = 100

rectangle(width, height)