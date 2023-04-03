# объявление функции
def is_pangram(text):
    txt = text.lower()
    alfa_result = []
    amount_of_word = 26
    for i in range(len(txt)):
        if txt[i] not in alfa_result and txt[i] != ' ':
            alfa_result.append(txt[i])
        else:
            continue
    if amount_of_word == len(alfa_result):
        return True
    else:
        return False
# считываем данные
text = 'Jackdaws love my big sphinx of quartz'

# вызываем функцию
print(is_pangram(text))