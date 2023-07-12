n = int(input())
m = int(input())

def get_max_index(n, m):
    matrix = [[int(i) for i in input().split()] for i in range(n)]
    tmp_max = -9999999999999
    for i in range(n):
        for j in range(m):
            if matrix[i][j] > tmp_max:
                tmp_max = matrix[i][j]
#    print(tmp_max)
    indexes = []
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == tmp_max:
                indexes.append(i)
                indexes.append(j)
    print(*indexes[0:2])
get_max_index(n, m)