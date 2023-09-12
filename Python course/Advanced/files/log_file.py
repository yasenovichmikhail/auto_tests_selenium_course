with open('C:/logfile.txt', encoding='utf-8') as input, open('C:/output.txt', 'w', encoding='utf-8') as output:
    for i in input:
        lst = i.strip().split(', ')
        # x = int(lst[2]) - int(lst[1])
        # print(lst)
        time1 = lst[1].split(':')
        time2 = lst[2].split(':')
        # if int(time2[0]) > int(time1[0]) and int(time2[1]) > int(time1[1]):

        # print(time1)
        # print(time2)
        x1 = time1[0] + time1[1]
        x2 = time2[0] + time2[1]
        # print(x1, x2)
        y = int(x2) - int(x1)
        if y >= 100:
            print(lst[0], end='\n', file=output)