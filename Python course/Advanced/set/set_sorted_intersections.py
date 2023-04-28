def get_identical_sorted_elements(text1, text2):
    str1 = [int(i) for i in text1.split()]
    str2 = [int(i) for i in text2.split()]

    myset = set(str1).intersection(str2)
    sorted_list = list(myset)
    sorted_list.sort()
    
    print(*sorted_list)

text1 = "1 7 8 9 7 3 10 6"
text2 = "6 4 3 2 7 3 10 5"

get_identical_sorted_elements(text1, text2)