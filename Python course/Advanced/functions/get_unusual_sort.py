

txt = '12 14 79 7 4 123 45 90 111'
lst = txt.split()

def get_sum(x):
    tmp = int(x)
    total_sum = 0
    while tmp > 0:
        last_digit = tmp % 10
        total_sum += last_digit
        tmp = tmp // 10
    return total_sum

result = sorted(lst, key=get_sum)
print(result)