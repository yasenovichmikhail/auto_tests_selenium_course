n = int(input())
k = int(input())
 
res = 0
for i in range(1, n+1):
    res = (res + k) % i
print(res + 1)