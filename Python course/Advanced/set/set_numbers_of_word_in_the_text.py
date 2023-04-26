def get_unique_letters(text):
    str1 = text.lower()
    str_result = ''
    for i in range(len(str1)):
        if str1[i] not in ('.,;:!?-'):
            str_result += str1[i]
        else:
            continue
    str2 = str_result.split()
    myset = set(str2)
    print(len(myset))

text = input()

get_unique_letters(text)