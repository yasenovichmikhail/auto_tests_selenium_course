import turtle, random

turtle.speed(0)
turtle.Screen().bgcolor('black')
turtle.up()
def star(size, x, y):
  turtle.goto(x, y)
  turtle.left(random.randint(0, 360))
  for _ in range(5):
    turtle.forward(size)
    turtle.right(144)

def play():
  for i in range(random.randint(50, 200)):
    side = random.randint(5, 20)
    x, y = (random.randint(-150, 150) for _ in '12')
    color = tuple(random.randint(0, 255) for _ in '123')
    turtle.fillcolor(color)
    turtle.begin_fill()
    star(side, x, y)
    turtle.end_fill()

play()