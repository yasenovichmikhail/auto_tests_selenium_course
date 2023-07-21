n = int(input())

def get_filling_4(n):
    matrix = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i <= j and i <= n - 1 -j:
                matrix[i][j] = 1
            elif i >= j and i >= n - 1 - j:
                matrix[i][j] = 1
    
    for i in matrix:
        print(*i)
    
get_filling_4(n)