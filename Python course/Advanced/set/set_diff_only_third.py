
def get_diff(n1, n2, n3):
    stroka1 = set(n1.split(' '))
    stroka2 = set(n2.split(' '))
    stroka3 = set(n3.split(' '))
    
    diff1 = stroka3.difference(stroka1)
    diff2 = stroka3.difference(stroka2)

    result = diff1.intersection(diff2)
    my_list = list(result)
    my_list.sort(key=int, reverse=True)
    print(*my_list)

str1 = '1 5 4 2 5 6 6 2 3 3 5 2'
str2 = '2 3 5 1 2 1 2 6 7 1 1 6'
str3 = '1 4 6 9 8 7 0 9 0 9 8 10'

get_diff(str1, str2, str3)