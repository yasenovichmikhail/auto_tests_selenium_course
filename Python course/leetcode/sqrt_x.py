import math


def get_rounded_sqrt(x):
    res = math.sqrt(x)
    return math.floor(res)


x = 8
print(get_rounded_sqrt(x))
