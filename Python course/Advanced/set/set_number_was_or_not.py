

def was_the_number(text):
    str1 = [int(i) for i in text.split()]
    list = []
    for i in range(len(str1)):
        if str1[i] in list:
            print('YES')
        else:
            list.append(str1[i])
            print('NO')

text = '1 2 3 002 03 4 5 05'

was_the_number(text)