def get_two_intersections_of_three(n1, n2, n3):
    stroka1 = set(n1.split(' '))
    stroka2 = set(n2.split(' '))
    stroka3 = set(n3.split(' '))
    
    one_two_intersection = stroka1.intersection(stroka2)
    result = one_two_intersection.difference(stroka3)
    my_list = list(result)
    my_list.sort(reverse=True, key=int)
    print(*my_list)

str1 = '4 2 5 10 6 2'
str2 = '10 4 7 6 3 10'
str3 = '1 2 1 5 9 5'

get_two_intersections_of_three(str1, str2, str3)