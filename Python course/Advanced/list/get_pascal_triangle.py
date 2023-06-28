def pascal(n):
    lst = []
    for k in range(0, n + 1):
        lst.append([1] + [0]*n)
    for i in range(1, n+1):
        for j in range(1, i+1):
            lst[i][j] = lst[i-1][j] + lst[i-1][j-1]
            # print(lst[i][j])
    for k in range(n, n +1):
        print(lst[n])

n = 3

pascal(n)