n, m = input().split()
n, m = int(n), int(m)

def get_sum_of_matrix(n, m):
    matrix1 = [[int(i) for i in input().split()] for i in range(n)] 
    empty_str = input()
    matrix2 = [[int(i) for i in input().split()] for i in range(n)]
    matrix3 = [[0] * m for k in range(n)]
    for i in range(n):
        for j in range(m):
            matrix3[i][j] = matrix1[i][j] + matrix2[i][j]
    for k in matrix3:
        print(*k)
    
get_sum_of_matrix(n, m)