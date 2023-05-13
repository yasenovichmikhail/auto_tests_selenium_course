def get_repeated_num(text):
    my_list = [int(i) for i in text.split()]
    my_set = set(my_list)
    result = len(my_list) - len(my_set)
    print(result)

text = '1 2 3 4 5 6 7 8 9 1 2 3'

get_repeated_num(text)