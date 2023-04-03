# объявление функции
def get_shipping_cost(quantity):
    cost = 1000
    extra_cost = 120
    counter = 0
    for i in range(quantity):
        if i == 0:
            counter += 1000
        elif i > 0:
            counter += 120
    return counter

# считываем данные
n = 3

# вызываем функцию
print(get_shipping_cost(n))