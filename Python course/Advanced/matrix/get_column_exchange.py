n = int(input())
m = int(input())

def get_column_exchange(n, m):
    matrix = [[int(i) for i in input().split()] for i in range(n)]
    row1, row2 = [int(k) for k in input().split()]
    for i in range(n):
        matrix[i][min(row1, row2)], matrix[i][max(row1, row2)] = matrix[i][max(row1, row2)], matrix[i][min(row1, row2)]
    for l in range(n):
        for h in range(m):
            print(matrix[l][h], end=' ')
        print()
    
get_column_exchange(n, m)