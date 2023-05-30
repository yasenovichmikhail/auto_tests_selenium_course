import random
import string

def get_postcode():
    my_list1 = []
    upper = string.ascii_uppercase
    for i in range(2):
        rnd = random.randint(0, 25)
        letter = upper[rnd]
        my_list1.append(letter)
    for j in range(1):
        rnd1 = random.randint(0, 99)
        my_list1.append(str(rnd1))
    my_list1.append('_')
    for k in range(1):
        rnd2 = random.randint(0, 99)
        my_list1.append(str(rnd2))
    for n in range(2):
        rnd3 = random.randint(0, 25)
        letter1 = upper[rnd3]
        my_list1.append(letter1)
    code = ''.join(my_list1)
    
    print(code)


get_postcode()





# LetterLetterNumber_NumberLetterLetter