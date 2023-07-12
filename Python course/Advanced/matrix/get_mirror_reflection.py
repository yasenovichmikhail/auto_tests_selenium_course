n = int(input())

def get_mirror_reflection(n):
    matrix = [[int(i) for i in input().split()] for i in range(n)]
    for i in range(n-1, -1, -1):
        print(*matrix[i], end=' ')
        print()
    
get_mirror_reflection(n)