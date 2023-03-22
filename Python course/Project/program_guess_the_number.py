import random

print('Добро пожаловать в числовую угадайку')
# chosen_border = int(input('Введите диапозон угадываемых цифр от 1 до 100: '))
number = random.randint(1, 100)


def is_valid(n):
    if n.isdigit() and 1 <= int(n) <= 100:
        return True
    else:
        return False

def is_valid_number():
    while True:
        x = input('Введите число от 1 до 100. Твое число: ')
        if is_valid(x) == True:
            return int(x)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')

def compare_num():
    counter = 0
    while True:
        input_digit = is_valid_number()
        counter += 1
        if input_digit < number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif input_digit > number:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            print('Количество попыток:', counter)
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
print(number)


def play_again():
    again = 'y'
    while again.lower() == 'y':
        again = input('Хотите попробовать еще раз? (y = yes, n = no): ') 
        if again == 'y':
            compare_num()
        else:
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

compare_num()
play_again()










