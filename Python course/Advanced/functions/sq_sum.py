def sq_sum(*args):
    lst = []
    for i in args:
        x = i ** 2
        lst.append(x)
    return sum(lst)


print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))