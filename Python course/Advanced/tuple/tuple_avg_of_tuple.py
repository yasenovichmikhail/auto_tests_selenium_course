numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
list_numbers = []
for i in range(len(numbers)):
    a = sum(numbers[i])
    b = len(numbers[i])
    x = a / b
    list_numbers.append(x)
print(list_numbers)
