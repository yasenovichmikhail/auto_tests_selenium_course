
def zhack_mystery():
    with open('C:/goats.txt', encoding='utf-8') as input:
        lst_color = []
        for i in input:
            if i.strip() != 'GOATS':
                lst_color.append(i.strip())
            else:
                break
    # print(lst_color)

        lst_goats = []

        for j in input:
            lst_goats.append(j.strip())
        my_dict = {}
        for k in lst_goats:
            my_dict[k] = my_dict.setdefault(k, 0) + 1  
    # print(my_dict)

        percent = int((len(lst_goats) * 7) / 100)
    # print(percent)

    with open('C:/answer.txt', 'w', encoding='utf-8') as output:
        for key, value in my_dict.items():
            if value > percent:
                print(key, end='\n', file=output)

zhack_mystery()
