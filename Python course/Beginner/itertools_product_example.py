from itertools import product

a = [int(i) for i in range(1, 10)]

b = [int(i) for i in range(1, 10)]

prod = product(a, b)
print(list(prod))


