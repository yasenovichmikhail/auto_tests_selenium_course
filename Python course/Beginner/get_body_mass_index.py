import math

def body_mass_index(weight, height):
    index_mass = weight / (height * height)
    if 18.5 <= index_mass <= 25:
        return print('Оптимальная масса')
    elif index_mass < 18.5:
        return print('Недостаточная масса')
    elif index_mass > 25:
        return print('Избыточная масса')

weight = 18.5
height = 1

body_mass_index(weight, height)

