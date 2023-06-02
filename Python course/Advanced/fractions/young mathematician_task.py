from fractions import Fraction as F
import math

def young_mathematician(n):
    lst = []
    my_tuple = ()
    result = []
    for i in range(1, n):
        a  = n - i
        b = i
        c = a + b
        if a < b:
            lst.append(F(a, b))
    for j in lst:
        if j.numerator + j.denominator == n:
            result.append(j)
    print(max(result))

n = 23

young_mathematician(n)