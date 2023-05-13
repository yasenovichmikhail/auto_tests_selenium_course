def is_exist_number(text1, text2):
    my_list1 = [int(i) for i in text1.split()]
    my_list2 = [int(i) for i in text2.split()]
    my_set1 = set(my_list1)
    my_set2 = set(my_list2)
    if my_set1 == my_set2:
        print('YES')
    else:
        print('NO')
    
text1 = input()
text2 = input()

is_exist_number(text1, text2)