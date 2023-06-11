import turtle

def get_web(n):
  x = 360 / n
  turtle.shape('triangle')
  for i in range(n):
      turtle.dot()
      turtle.forward(100)
      turtle.stamp()
      turtle.backward(100)
      turtle.left(x)

n = 8

get_web(n)