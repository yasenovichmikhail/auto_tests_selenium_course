x, y = input()
n = 8
matrix = [['.'] * n for _ in range(n)]
y = n - int(y)
x = ord(x) - 97

for i in range(n):
    for j in range(n):
        if i == y or j == x:
            matrix[i][j] = '*'
        elif (i + j == y + x) or (i - j == y -x):
            matrix[i][j] = '*'
            
matrix[y][x] = 'Q'
for x in range(n):
    print(*matrix[x])