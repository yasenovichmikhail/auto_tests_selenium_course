
n = int(input())
m = int(input())

matrix = [[input() for _ in range(m)] for _ in range(n)]

for i in matrix:
    print(*i)