stroka = input().split()
n = int(input())
lst = [[] * n for _ in range(n)]

for i in range(n):
    for j in range(i, len(stroka), n):
        lst[i].append(stroka[j])
        
print(lst)