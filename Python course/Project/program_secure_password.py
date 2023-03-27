import random

DIGITS  = '0123456789'
LOWERCASE_LETTERS  = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS  = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION  = '!#$%&*+-=?@^_.'

chars = ''
chars_new = ''

count_pass = input('Укажите количество паролей для генерации: ')
len_pass = input('Укажите длину одного пароля: ')
digit_on = input('Включать ли цифры 0123456789? (y/n): ')
if digit_on.lower() == 'y':
    chars += DIGITS
upper_on = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n): ')
if upper_on.lower() == 'y':
    chars += UPPERCASE_LETTERS
lower_on = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n): ')
if lower_on.lower() == 'y':
    chars += LOWERCASE_LETTERS
char_on = input('Включать ли символы !#$%&*+-=?@^_? (y/n): ')
if char_on.lower() == 'y':
    chars += PUNCTUATION
exc_replace = input('Исключать ли неоднозначные символы il1Lo0O? (y/n): ')
if exc_replace.lower() == 'y':
    for i in range(len(chars)):
        if chars[i] not in 'il1Lo0O':
            chars_new += chars[i]


def generate_password(length, chars):
    s = ''
    while len(s) != length:
        x = random.choice(chars)
        s += x
    print(s)
print(generate_password(7, chars_new))