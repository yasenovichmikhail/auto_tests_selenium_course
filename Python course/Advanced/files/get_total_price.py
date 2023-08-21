
from functools import reduce

def get_total_price():
    file = open('C:/prices.txt', encoding='utf-8')
    total = 0
    lst = []
    for line in file:
        prices = line.rstrip().split('\t')
        tmp_total = int(prices[1]) * int(prices[2])
        lst.append(tmp_total)
        total = reduce(lambda a, b: a + b, lst)
    print(total)
    
    file.close()
    
get_total_price()