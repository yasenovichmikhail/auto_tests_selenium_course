import turtle

turtle.Screen().setup(400, 400)               # устанавливаем размер граф. окна
turtle.Screen().addshape('rocketship.png')    # добавляем форму черепашки

turtle.Screen().bgpic('space.jpg')            # устанавливаем фоновое изображение
turtle.shape('rocketship.png')                # устанавливаем форму черепашки
turtle.pencolor('green')
turtle.pensize(5)

for _ in range(4):
  turtle.forward(150)
  turtle.left(90)