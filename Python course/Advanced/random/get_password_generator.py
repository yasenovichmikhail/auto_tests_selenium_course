
import random

length = 15
password = ''

for i in range(length):
    lower = random.randint(97, 122)
    upper = random.randint(65, 90)
    choose = random.randint(1, 2)
    if choose == 1:
        password += chr(lower)
    else:
        password += chr(upper)
        
print(password)