x = 1
y = 25

def get_interested_num(x, y):
    lst = []
    for i in range(x, y+1):
        if '0' not in str(i):
            lst.append(i)
    for i in lst:
        if all([i % int(n) == 0 for n in str(i)]):
            print(i, end=' ')

get_interested_num(x, y)