n = int(input())

def get_snowflake(n):
    matrix = [['.'] * n for i in range(n)]
#    print(matrix)
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = '*'
            elif j == n - i - 1:
                matrix[i][j] = '*'
            elif i==j or i==n-1-j or i==n//2 or j==n//2:
                matrix[i][j] = '*'
    for i in matrix:
        print(*i)
    
get_snowflake(n)