n = 10
list = []
f1, f2, f3 = 1, 1, 1
for i in range(n):
    list.append(f1)
    f1, f2, f3 = f2, f3, f1 + f2 + f3
print(*list)

# фибоначчи
# n = 10
# f1, f2 = 1, 1
# for i in range(n):
#     print(f1)
#     f1, f2 = f2, f1 + f2



