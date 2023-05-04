
def get_not_exist_grades(n1, n2, n3):
    stroka1 = set(n1.split(' '))
    stroka2 = set(n2.split(' '))
    stroka3 = set(n3.split(' '))
    my_str = '0 1 2 3 4 5 6 7 8 9 10'.split(' ')
    my_set = set(my_str)
    
    diff1 = my_set.difference(stroka1)
    diff2 = my_set.difference(stroka2)
    diff3 = my_set.difference(stroka3)
    
    result = diff1.intersection(diff2, diff3)
    my_list = list(result)
    my_list.sort(key=int)
    print(*my_list)

str1 = '1 5 4 2 5 6 6 2 3 3 5 2'
str2 = '2 3 5 1 2 1 2 6 7 1 1 6'
str3 = '1 4 6 8 8 7 0 6 0 3 8 1'

get_not_exist_grades(str1, str2, str3)