n = int(input())

def get_more_than_avg(n):
    matrix = [[int(i) for i in input().split()] for _ in range(n)]
    for i in matrix:
        x = sum(i) / len(i)
        counter = 0
        for j in i:
            if j > x:
                counter += 1
        print(counter)
    
get_more_than_avg(n)