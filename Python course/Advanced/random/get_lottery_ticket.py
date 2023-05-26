
import random

x = 7
result = []

for i in range(x):
    number = random.randint(1, 49)
    result.append(number)
result.sort()

print(*result)