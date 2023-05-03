
def get_symmetric_diff(n1, n2, n3):
    stroka1 = set(n1.split(' '))
    stroka2 = set(n2.split(' '))
    stroka3 = set(n3.split(' '))
    
    sym_diff1 = stroka1.symmetric_difference(stroka2)
    sym_diff2 = stroka2.symmetric_difference(stroka3)
    sym_diff3 = stroka3.symmetric_difference(stroka1)

    result = sym_diff1.union(sym_diff2, sym_diff3)
    my_list = list(result)
    my_list.sort(key=int)
    print(*my_list)

str1 = '1 5 4 2 5 6 6 2 3 3 5 2'
str2 = '2 3 5 10 2 10 2 6 7 10 10 6'
str3 = '1 4 6 9 8 7 0 9 0 9 8 10'

get_symmetric_diff(str1, str2, str3)