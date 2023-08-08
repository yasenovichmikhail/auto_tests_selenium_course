n = int(input())

def get_matrix_transposition(n):
    matrix = [[int(i) for i in input().split()] for i in range(n)]
    for i in range(n):
        for j in range(n):
            print(matrix[j][i], end=' ')
        print()
    
get_matrix_transposition(n)