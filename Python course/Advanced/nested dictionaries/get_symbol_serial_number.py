s = input().split()
result = {}

for i in s:
    result[i] = result.get(i, 0) + 1
    print(result[i], end = ' ')