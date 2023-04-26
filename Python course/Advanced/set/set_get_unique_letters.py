
def get_unique_letters():
    for i in range(int(input())):
        str = '' + input()
        str1 = str.lower()
        myset = set(str1)
        print(len(myset))

get_unique_letters()