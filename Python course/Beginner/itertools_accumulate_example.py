from itertools import accumulate
import operator

lst = [i for i in range(1, 8)]

sum = accumulate(lst)
mul = accumulate(lst, func=operator.mul)

print(lst)
print(list(sum))
print (list(mul))
