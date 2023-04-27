def get_identical_elements(text1, text2):
    str1 = [int(i) for i in text1.split()]
    str2 = [int(i) for i in text2.split()]
    myset = set(str1).intersection(str2)
    
    print(len(myset))

text1 = "1 7 3 8 10 2 5"
text2 = "6 5 2 8 4 3 7"

get_identical_elements(text1, text2)