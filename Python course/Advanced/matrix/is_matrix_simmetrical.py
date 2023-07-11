n = 5

def is_matrix_simmetrical(n):
    matrix = [[5, 3, 7, 1, 5], [3, 5, 4, 5, 7], [7, 4, 4, 8, 4], [1, 5, 8, 5, 1], [5, 7, 4, 1, 5]]
    right_top = []
    left_bottom = []
    Flag = True
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                Flag = False
                break
    if Flag == False:
        print('No')
    else:
        print('Yes')
    
is_matrix_simmetrical(n)