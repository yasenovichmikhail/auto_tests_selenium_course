n = int(input())

def get_sum_of_quarters(n):
    matrix = [[int(i) for i in input().split()] for  i in range(n)]
    top = []
    bottom = []
    right = []
    left = []
    for i in range(n):
        for j in range(n):
            if i < j and i < n - 1 - j:
                top.append(matrix[i][j])
            elif i > j and i > n - 1 - j:
                bottom.append(matrix[i][j])
            elif i > j and i < n - 1 - j:
                left.append(matrix[i][j])
            elif i < j and i > n - 1 - j:
                right.append(matrix[i][j])
    top = sum(top)
    bottom = sum(bottom)
    right = sum(right)
    left = sum(left)
    print(f"Верхняя четверть: {top}")
    print(f"Правая четверть: {right}")
    print(f"Нижняя четверть: {bottom}")
    print(f"Левая четверть: {left}")
    
get_sum_of_quarters(n)