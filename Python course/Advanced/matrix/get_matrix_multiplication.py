def matrix_multiplication():
    n, m = input().split()
    n, m = int(n), int(m)
    matrix1 = [[int(i) for i in input().split()] for i in range(n)] 
    empty_str = input()
    m, k = input().split()
    m, k = int(m), int(k)
    matrix2 = [[int(j) for j in input().split()] for j in range(m)]
    matrix3 = [[0] * k for j in range(n)]
    for i in range(n):
        for j in range(k):
            for o in range(m):
                matrix3[i][j] += matrix1[i][o] * matrix2[o][j]
    for mtrx in matrix3:
        print(*mtrx)
    
matrix_multiplication()