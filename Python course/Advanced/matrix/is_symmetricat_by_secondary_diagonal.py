n = int(input())

def is_matrix_simmetrical(n):
    matrix = [[int(i) for i in input().split()] for i in range(n)]
    right_top = []
    left_bottom = []
    Flag = True
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[n-j-1][n-i-1]:
                Flag = False
                break
    if Flag == False:
        print('NO')
    else:
        print('YES')
    
is_matrix_simmetrical(n)