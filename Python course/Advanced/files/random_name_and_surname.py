import random

with open('C:/last_names.txt', encoding='utf-8') as last_name, open('C:/first_names.txt', encoding='utf-8') as first_names:
    last_name = [i.strip() for i in last_name.readlines()]
    first_names = [j.strip() for j in first_names.readlines()]
    for i in range(3):
        rnd_first_name = random.sample(first_names, 1)
        rnd_last_name = random.sample(last_name, 1)
        print(*rnd_first_name, *rnd_last_name)