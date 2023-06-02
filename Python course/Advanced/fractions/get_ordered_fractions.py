from fractions import Fraction as F

def get_ordered_fractions(n):
    lst = []
    my_tuple = ()
    result = []
    for i in range(1, n+1):
        # print(i)
        for j in range(1, n):
            # print(j)
            if 0 < j / i < 1:
                if F(j, i) not in lst:
                    lst.append(F(j, i))
                else:
                    continue
    lst.sort()
    print(*lst, sep='\n')

n = 5

get_ordered_fractions(n)