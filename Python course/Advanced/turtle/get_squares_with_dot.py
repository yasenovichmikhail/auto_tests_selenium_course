import turtle

def get_squares_with_dot():
  for i in range(2):
      turtle.dot()
      turtle.forward(60)
      turtle.dot()
      turtle.left(90)
      turtle.forward(30)
      turtle.left(90)

get_squares_with_dot()