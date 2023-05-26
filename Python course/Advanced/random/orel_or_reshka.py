
import random

value = 7

for i in range(value):
    x = random.randrange(0, 2)
    if x == 0:
        print('Орел')
    else:
        print('Решка')