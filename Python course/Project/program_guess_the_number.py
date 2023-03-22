import random

print('Добро пожаловать в числовую угадайку')
print('Необходимо определить диапозон угадываемых цифр')
rihgt_border = int(input('Диапозон угадываемых цифр будет от 1 до: '))


def is_valid(n):
    if n.isdigit() and 1 <= int(n) <= rihgt_border:
        return True
    else:
        return False

def is_valid_number():
    while True:
        x = input(f'Введите число от 1 до {rihgt_border}. Твое число: ')
        if is_valid(x) == True:
            return int(x)
        else:
            print(f'А может быть все-таки введем целое число от 1 до {rihgt_border}?')

def compare_num(border):
    number = random.randint(1, border)
    counter = 0
    while True:
        input_digit = is_valid_number()
        counter += 1
        if input_digit < number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            print(number)
        elif input_digit > number:
            print('Ваше число больше загаданного, попробуйте еще разок')
            print(number)
        else:
            print('Вы угадали, поздравляем!')
            print('Количество попыток:', counter)
            break

compare_num(rihgt_border)

def play_again():
    again = 'y'
    while again.lower() == 'y':
        again = input('Хотите попробовать еще раз? (y = yes, n = no): ') 
        if again == 'y':
            compare_num(rihgt_border)
        else:
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

play_again()









