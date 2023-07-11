n = int(input())                                                

def is_magic_squares(n):
    matrix = [[int(i) for i in input().split()] for i in range(n)]  
    matrix_90 = [[[] for i in range(n)] for i in range(n)]           
    count = 0                  
    diag_main = []            
    diag = []                  
    lst = []                   
    for i in range(n):
        diag_main.append(matrix[i][i])              
        diag.append(matrix[i][n - i - 1])           
        for j in range(n):
            matrix_90[i][j] = matrix[n - j - 1][i]  
            if matrix[i][j] not in lst:
                lst.append(matrix[i][j])            
    for i in range(n):
        if sum(matrix[i]) == sum(matrix_90[i]) == sum(diag_main) == sum(diag):
            count += 1
    print('YES' if count == n and len(lst) == n ** 2 and 0 not in lst else 'NO')

is_magic_squares(n)