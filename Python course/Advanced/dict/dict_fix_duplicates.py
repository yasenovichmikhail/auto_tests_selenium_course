
def fix_duplicates(text):
    my_list = text.split()
    my_dict = {}
    list1 = []
    # print(my_list)
    for i in my_list:
        my_dict[i] = my_dict.get(i, -1) + 1
        # print(my_dict)
        if my_dict[i] == 0:
            # print(i)
            list1.append(i)
        else:
            # print(f'{i}_{my_dict[i]}')
            list1.append(f'{i}_{my_dict[i]}')
    print(*list1)

text = 'a b c a a d c'

fix_duplicates(text)