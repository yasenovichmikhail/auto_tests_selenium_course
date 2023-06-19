import turtle, math

turtle.speed(0)
def figure(n, side, color):
  s = 180 - 180 * (n - 2) / n
  turtle.fillcolor(color)
  turtle.begin_fill()
  for i in range(n):
    turtle.forward(side)
    turtle.right(s)
  turtle.end_fill()

turtle.up()
turtle.goto(0, 100)
figure(8, 100, 'black')
turtle.goto(3, 94)
figure(8, 95, 'white')
turtle.goto(6, 88)
figure(8, 90, 'red')

turtle.goto(-50, -50)
turtle.fillcolor('white')
turtle.begin_fill()
turtle.write('STOP', font=('Arial', 57, 'bold'))
turtle.end_fill()