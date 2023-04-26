def get_unique_letters():
    result = ''
    for i in range(int(input())):
        str = '' + input()
        str1 = str.lower()
        result += str1
        set_result = set(result)
    print(len(set_result))

get_unique_letters()