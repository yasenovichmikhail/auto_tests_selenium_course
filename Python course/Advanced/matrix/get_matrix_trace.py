n = int(input())

def get_matrix_trace(n):
    matrix = [[int(_) for _ in input().split()] for __ in range(n)]
    counter = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                counter += matrix[i][j]
    print(counter)
    
get_matrix_trace(n)