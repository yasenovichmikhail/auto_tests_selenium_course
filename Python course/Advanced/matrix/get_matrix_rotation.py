n = int(input())

def get_matrix_rotation(n):
    matrix = [[int(i) for i in input().split()] for i in range(n)]
    for i in range(n):
        for j in range(-1, -n-1, -1):
            print(matrix[j][i], end=' ')    
        print()
    
get_matrix_rotation(n)