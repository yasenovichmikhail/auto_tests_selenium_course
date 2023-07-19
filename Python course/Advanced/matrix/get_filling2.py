n, m = input().split()
n, m = int(n), int(m)

def get_filling(n, m):
    matrix = [[0] * m for i in range(n)]
    counter = 0
    for j in range(m):
        for i in range(n):
            if matrix[i][j] == 0:
                counter +=1
                matrix[i][j] = counter
    for i in range(n):
        for j in range(m):
            print(str(matrix[i][j]).ljust(3), end='')
        print()
    
get_filling(n, m)