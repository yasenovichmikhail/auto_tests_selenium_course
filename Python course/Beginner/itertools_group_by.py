from itertools import groupby

def smaller_than_50(x):
    return x < 50

lst = [i for i in range(100)]

group = groupby(lst, key=smaller_than_50)

for key, value in group:
    print(key, list(value))