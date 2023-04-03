import math


def get_winners(n, k):
    for i in range(1, n + 1):
        x = i**k
        while x < 41:
            print(x)


n = 41
k = 2

get_winners(n, k)

