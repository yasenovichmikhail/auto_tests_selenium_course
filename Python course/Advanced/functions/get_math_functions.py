
from math import sin
def func(n, op):
    sl = dict(квадрат=n ** 2, куб=n ** 3, корень=n ** 0.5, модуль=abs(n), синус=sin(n))
    return sl[op]

n = 5
op = 'квадрат'

print(func(n, op))