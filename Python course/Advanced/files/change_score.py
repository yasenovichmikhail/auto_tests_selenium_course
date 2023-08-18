with open('C:/class_scores.txt', encoding='utf-8') as input:
    lst = [i.strip() for i in input]
    # print(lst)

with open('C:/new_scores.txt', 'w', encoding='utf-8') as output:
    new_lst = [i.split() for i in lst]
    for index, item in new_lst:
        if int(item) + 5 <=100:
            print(index, int(item) + 5, end='\n', file=output)
        else:
            print(index, 100, end='\n', file=output)