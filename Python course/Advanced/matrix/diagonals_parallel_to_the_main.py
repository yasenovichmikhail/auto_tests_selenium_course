n = int(input())

def diagonals_parallel_to_the_main(n):
    matrix = [[0]*n for i in range(n)]

    for i in range(n):
        for j in range(n):
            if j > i:
                matrix[i][j] = j - i
            elif i > j:
                matrix[i][j] = i - j
            
    for i in range(n):
        print(*matrix[i])
    
diagonals_parallel_to_the_main(n)