n = int(input())
a = [list(map(int, list(input().split()))) for _ in range(n)]
m = int(input())

def multi(a, b):
    n = len(a)
    b = list(zip(*b))
    return [[sum([a[i][r] * b[j][r] for r in range(n)]) for j in range(n)] for i in range(n)]

def expo(a, m):
    c = list(a)
    for _ in range(m-1):
        c = multi(c, a)
    return c

result = expo(a, m)

[print(*row) for row in result]