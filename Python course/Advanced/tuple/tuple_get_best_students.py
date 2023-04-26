s = [input() for _ in range(int(input()))]
print(*s, sep='\n')
print()
list1 = []
for i in range(len(s)):
    if int(s[i][-1]) > 3:
        list1.append(s[i])
print(*list1, sep='\n')