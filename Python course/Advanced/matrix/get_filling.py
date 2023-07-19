n, m = input().split()
n, m = int(n), int(m)

def get_filling(n, m):
    matrix = [[0] * m for i in range(n)]
    counter = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                counter +=1
                matrix[i][j] = counter
                print(str(matrix[i][j]).ljust(3), end='')
        print()
    
get_filling(n, m)