n = int(input())

def side_diagonal(n):
    matrix = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i + j == n - 1:
                matrix[i][j] = 1
                
    for i in range(n):
        for j in range(n):
            if i + j >= n:
                matrix[i][j] = 2
             
    for row in matrix:
        print(*row)

side_diagonal(n)