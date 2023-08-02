import random

with open('C:/random.txt', 'w', encoding='utf-8') as file:
    lst_random = [random.randint(111, 778) for i in range(25)]
    print(*lst_random, sep='\n', file=file)

    
