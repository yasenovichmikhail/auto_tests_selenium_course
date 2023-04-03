# объявление функции
def solve(a, b, c):
    import math
    d = b**2 - 4*a*c
    t1 = (-b + math.sqrt(d))/(2*a)
    t2 = (-b - math.sqrt(d))/(2*a)
    return min(t1, t2), max(t1, t2)

# считываем данные
a, b, c = 1, 2, 1

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)