

direction = input('Что мы должны сделать: шифровать или дешифровать? \n').lower()
while direction != 'шифровать' and direction != 'дешифровать':
    direction = input("Будь внимателен! Введи 'шифровать' или 'дешифровать' \n")
lang = input('Выбери язык шифрования: русский или английский: \n').lower()
while lang != 'русский' and lang != 'английский':
    lang = input("Будь внимателен! Введи 'русский' или 'английский' \n")
step = input('Укажите шаг сдвига шифрования: \n')
while step.isdigit() != True:
    step = input("Будь внимателен! Введи число: \n")
text = input('Введите текст для обработки: \n')
while text.isspace() == True:
    text = input('Будь внимателен! Введи текст: \n')


def caesar(direction, language, step, text):

    upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

    # Объявляем цикл for. Количество итераций равно длине строки text.
    for i in range(len(text)):

        if language == 'русский':
            alphas = 32
            low_alphabet = lower_rus_alphabet
            upp_alphabet = upper_rus_alphabet
        if language == 'английский':
            alphas = 26
            low_alphabet = lower_eng_alphabet
            upp_alphabet = upper_eng_alphabet


        if text[i].isalpha():

            if text[i] == text[i].lower():
                place = low_alphabet.index(text[i])
            if text[i] == text[i].upper():
                place = upp_alphabet.index(text[i])

            if direction == 'дешифровать':
                # Новый ндекс = Старый индекс - Шаг % Длина алфавита
                index = (place - int(step)) % alphas

            elif direction == 'шифровать':
                index = (place + int(step)) % alphas


            # Выводим измененный символ.
            if text[i] == text[i].lower():
                print(low_alphabet[index], end='')
            if text[i] == text[i].upper():
                print(upp_alphabet[index], end='')            



        # Если text[i] не является буквой:
        else:
            # Делаем print этого символа без изменений.
            print(text[i], end='')
        
caesar(direction, lang, step, text)
