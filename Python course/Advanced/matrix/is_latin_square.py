n = int(input())

def is_latin_square(n):
    matrix = [[int(i) for i in input().split()] for i in range(n)]
    counter = 0
    Flag = True
    latin_list = [i for i in range(1, n + 1)]
    

    for i in range(n):
        x = sorted(matrix[i])
        y = sorted(matrix[q][i] for q in range(n))

        if x != latin_list or y != latin_list:
            Flag = False
            break
    
    if Flag:
        print('YES')
    else:
        print('NO')

is_latin_square(n)