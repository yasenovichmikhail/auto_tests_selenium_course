
txt = '111 14 79 7 4 123 90 45 12 171'
lst = txt.split()
lst1 = [int(i) for i in lst]
lst1.sort()
print(lst1)

def get_sum(x):
    tmp = int(x)
    total_sum = 0
    while tmp > 0:
        last_digit = tmp % 10
        total_sum += last_digit
        tmp = tmp // 10
    return total_sum

result = sorted(lst1, key=get_sum)
print(*result)