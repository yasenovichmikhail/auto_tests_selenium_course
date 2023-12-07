lst = [i for i in range(1, 7)]

result = filter(lambda x: x % 2 == 0, lst)

result1 = [i for i in lst if i % 2 == 0]

print(list(result))
print(result1)