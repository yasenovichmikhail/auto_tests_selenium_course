n = int(input())

def get_diagonals_exchange(n):
    matrix = [[int(i) for i in input().split()] for i in range(n)]
    for i in range(len(matrix)):
        main_d = matrix[i][i]
        matrix[i][i] = matrix[n-1-i][i]
        matrix[n-1-i][i] = main_d
    for j in matrix:
        print(*j)
    print()
    
get_diagonals_exchange(n)