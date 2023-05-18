def is_bad_day(text1, text2):
    my_list1 = [int(i) for i in text1.split()]
    my_list2 = [int(i) for i in text2.split()]
    my_set1 = set(my_list1)
    my_set2 = set(my_list2)
    if len(my_set1.intersection(my_set2)) > 0:
        result = my_set1.intersection(my_set2)
        sorted_result = sorted(result, reverse=True)
        print(*sorted_result)
    else:
        print('BAD DAY')
    
text1 = input()
text2 = input()

is_bad_day(text1, text2)