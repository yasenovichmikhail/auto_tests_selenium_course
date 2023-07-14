n = int(input())

def get_max_in_the_lower_area(n):
    matrix = [[int(i) for i in input().split()] for i in range(n)]
#    print(matrix)
    lst = []
    for i in range(n):
        for j in range(n):
            if i > j or i == j:
                lst.append(matrix[i][j])
    print(max(lst))
                
    
get_max_in_the_lower_area(n)