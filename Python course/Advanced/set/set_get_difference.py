def get_diff_between_sets(text1, text2):
    str1 = [int(i) for i in text1.split()]
    str2 = [int(i) for i in text2.split()]

    myset = set(str1).difference(str2)
    
    sorted_list = list(myset)
    sorted_list.sort()
    
    print(*sorted_list)

text1 = "1 34 56 78 90 123 444 55452 23456"
text2 = "341 434 56 1 34"

get_diff_between_sets(text1, text2)