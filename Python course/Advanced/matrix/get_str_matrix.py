
n = int(input())
m = int(input())
matrix = [[0]*m for i in range(n)]

for i in range(n):                     # выводим матрицу
    for j in range(m):
        matrix[i][j] = input()
    print(*matrix[i])
        
for j in range(m):
    for i in range(n):                
        print(matrix[i][j], end=' ')
    print()