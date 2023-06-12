def matrix(a=1, b=None, c=0):
    lst = []
    for i in range(a):
        if b == None:
            b = a
            lst.append([c] * (b))
        else:
            lst.append([c] * (b))

    return lst


print(matrix())

matrix()
