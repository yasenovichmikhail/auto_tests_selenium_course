
import random

def generate_password(m):
    password = ''
    restricted = 'lI1oO0'
    while len(password) != m:
        lower = random.randint(97, 122)
        upper = random.randint(65, 90)
        digits = random.randint(0, 9)
        choose = random.randint(1, 3)
        if choose == 1:
            if chr(lower) not in restricted:
                password += chr(lower)
        elif choose == 2:
            if chr(upper) not in restricted:
                password += chr(upper)
        else:
            if str(digits) not in restricted:
                password += str(digits)
    return(password)

def generate_passwords(n, m):
    for j in range(n):
        print(generate_password(m))

n = 9
m = 7

generate_passwords(n, m)