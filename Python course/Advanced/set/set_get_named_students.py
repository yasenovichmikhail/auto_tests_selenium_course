def get_named_students(text1, text2):
    my_list1 = [i for i in text1.split()]
    my_list2 = [i for i in text2.split()]
    my_set1 = set(my_list1)
    my_set2 = set(my_list2)
    result = sorted(my_set1.union(my_set2))
    print(*result)
text1 = input()
text2 = input()

get_named_students(text1, text2)