import random
choices = ['камень', 'бумага', 'ножницы']
def get_winners(timur, ruslan):
    if timur == choices[0] and ruslan == choices[1]:
        print('Руслан')
    elif timur == choices[1] and ruslan == choices[2]:
        print('Руслан')
    elif timur == choices[2] and ruslan == choices[0]:
        print('Руслан')
    elif ruslan == choices[0] and timur == choices[1]:
        print('Тимур')
    elif ruslan == choices[1] and timur == choices[2]:
        print('Тимур')
    elif ruslan == choices[2] and timur == choices[0]:
        print('Тимур')
    else:
        print('ничья')

stroka1 = random.choice(choices)
stroka2 = random.choice(choices)

get_winners(stroka1, stroka2)