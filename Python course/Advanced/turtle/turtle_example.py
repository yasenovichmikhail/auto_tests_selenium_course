import turtle
window = turtle.Screen()

turtle.showturtle()

print(turtle.heading())
turtle.setheading(180)
print(turtle.heading())

turtle.shape('square')
turtle.forward(100)
turtle.setheading(90)

turtle.Screen().addshape('rocketship.gif')  # регистрируем изображение
turtle.shape('rocketship.gif')              # устанавливаем изображение

for _ in range(4):
  turtle.forward(150)
  turtle.left(90)

window.exitonclick()