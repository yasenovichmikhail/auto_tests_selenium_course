n = int(input())
m = int(input())

def get_multiplication_table(n, m):
    mult = [[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            mult[i][j] = i * j
    for k in range(n):
        for l in range(m):
            print(str(mult[k][l]).ljust(3), end='')
        print()
    
get_multiplication_table(n, m)