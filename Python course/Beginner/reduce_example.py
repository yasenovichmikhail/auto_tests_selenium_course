from functools import reduce

lst = [i for i in range(1,7)]

product_lst = reduce(lambda x, y: x * y, lst)

print(product_lst)