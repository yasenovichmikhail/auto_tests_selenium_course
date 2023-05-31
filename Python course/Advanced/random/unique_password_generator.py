
import random
import string

def generate_password(m):
    lower = 'abcdefghijkmnpqrstuvwxyz'
    upper = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
    digits = '23456789'
    my_list = []
    lower1 = random.choice(lower)
    my_list.append(lower1)
    upper1 = random.choice(upper)
    my_list.append(upper1)
    digits1 = random.choice(digits)
    my_list.append(digits1)
    while len(my_list) != m:
        choice = random.randint(1, 3)
        if choice == 1:
            x = random.choice(lower) 
            my_list.append(x)
        elif choice == 2:
            x1 = random.choice(upper)
            my_list.append(x1)
        elif choice == 3:
            x2 = random.choice(digits)
            my_list.append(x2)
    random.shuffle(my_list)
    print(*my_list, sep='')

def generate_passwords(n, m):
    for j in range(n):
        generate_password(m)

n = 9
m = 7

generate_passwords(n, m)