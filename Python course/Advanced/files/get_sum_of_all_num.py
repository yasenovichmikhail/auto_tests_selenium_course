with open('C:/nums.txt', encoding='utf-8') as file:
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    digits = '1234567890'
    tmp_str = ''
    for i in file:
        for j in i:
            if j in digits:
                tmp_str += j
            else:
                tmp_str += ' '
    
    lst = [int(i) for i in tmp_str.split()]
    
    print(sum(lst))