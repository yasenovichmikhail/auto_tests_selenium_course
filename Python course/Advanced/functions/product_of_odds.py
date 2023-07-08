from functools import reduce

def product_of_odds(data):
    result = reduce(lambda a, b: a * b if b % 2 == 1 else a + 0, data, 1)
    print(result)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

product_of_odds(data)
