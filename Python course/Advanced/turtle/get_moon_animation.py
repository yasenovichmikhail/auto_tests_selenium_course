import turtle

turtle.bgcolor('darkblue')
turtle.penup()
turtle.speed(0)  # Настройка основных значений
turtle.dot(200, 'gold3')
turtle.forward(200)
turtle.shape('circle')
turtle.shapesize(10)
turtle.color('darkblue')
while True:  # Цикл прохода черепашки справа налево
    for _ in range(400):
        turtle.backward(1)
    turtle.forward(400)