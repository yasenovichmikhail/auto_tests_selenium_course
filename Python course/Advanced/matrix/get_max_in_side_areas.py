n = int(input())

def get_max_in_side_areas(n):
    matrix = [[int(i) for i in input().split()] for i in range(n)]
    lst_result = []
    for i in range(n):
        for j in range(n):
            if i >= j and i <= n - 1 - j:
                lst_result.append(matrix[i][j])
            elif i <= j and i >= n -1 -j:
                lst_result.append(matrix[i][j])
    print(max(lst_result))
get_max_in_side_areas(n)