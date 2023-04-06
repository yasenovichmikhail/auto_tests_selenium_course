def get_unique_numbers(s):
    list = s.split()
    list_unique = []
    for i in range(len(list)):
        if list[i] in list_unique:
            continue
        else:
            list_unique.append(list[i])
    print(len(list_unique)) 


s = '1 1 1 2 2 2 2 3 3 3 5 6 7 8'

get_unique_numbers(s)