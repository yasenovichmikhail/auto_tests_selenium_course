from functools import reduce

with open('C:/numbers.txt', encoding='utf-8') as file:
    for i in file:
        line = i.strip().split()
        sum_of_line = reduce(lambda a, b: int(a) + int(b), line)
        print(sum_of_line)