# объявление функции
import math
def get_factorial(n):
    return int(math.factorial(n))
    
def compute_binom(n, k):
    return int(get_factorial(n) / (get_factorial(k)*get_factorial(n - k)))

# считываем данные
n = int(1)
k = int(1)

# вызываем функцию
print(compute_binom(n, k))