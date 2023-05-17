
def get_the_most_famous_word(s):
    text = s.lower()
    my_text = ''
    alpha_eng = 'abcdefghijklmnopqrstuvwxyz '
    alpha_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    result = {}
    my_list = []
    for i in text:
        if i in alpha_eng or i in alpha_ru:
            my_text +=i
        else:
            continue
    my_text = my_text.split(' ')
    for num in my_text:
        result[num] = result.get(num, 0) + 1
    tmp = 99999999999999999
    for key, value in result.items():
        if value < tmp:
            tmp = value
    for key1, value1 in result.items():
        if value1 == tmp:
            my_list.append(key1)
    my_list_result = min(my_list)
    print(my_list_result)

s = 'home sweet home sweet.'

get_the_most_famous_word(s)