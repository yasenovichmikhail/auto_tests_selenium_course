
def get_developers_dictionary(n):
    list1 = []
    list2 = []
    for i in range(n):
        txt1 = input() 
        list_or = txt1.split(': ')
        txt_lo = txt1.lower()
        list_lo = txt_lo.split(': ')
        list1.append(list_lo[0])
        list2.append(list_or[1])
    my_dict = dict(zip(list1, list2))
    m = int(input())
    for j in range(m):
        srch_word = input().lower()
#        print(srch_word)
        def is_in_dict(srch_word, my_dict):
            if srch_word in my_dict:
                return True
            else:
                return False
#        print(is_in_dict(srch_word, my_dict))
        if is_in_dict(srch_word, my_dict):
            for key, value in my_dict.items():
                if srch_word == key:
                    print(value)
        else:
            print('Не найдено')
n = int(input())

get_developers_dictionary(n)