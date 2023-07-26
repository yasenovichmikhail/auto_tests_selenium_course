n, m = [int(i) for i in input().split()]
mtx = [[0] * m for _ in range(n)]
sequence, k = 1, 0

while sequence != n * m + 1:
    for i in range(n):
        for j in range(m):
            if i + j == k:
                mtx[i][j] = sequence
                sequence += 1
    k += 1

for i in range(n):
    for j in range(m):
        print(str(mtx[i][j]).ljust(3), end='')
    print()