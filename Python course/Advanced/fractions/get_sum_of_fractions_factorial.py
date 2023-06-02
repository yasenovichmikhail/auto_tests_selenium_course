from fractions import Fraction as F
import math

def get_sum_of_fractions(n):
    res = 0
    for i in range(0, n):
        res += F(1, math.factorial(i + 1))
    print(res)

n = 3

get_sum_of_fractions(n)