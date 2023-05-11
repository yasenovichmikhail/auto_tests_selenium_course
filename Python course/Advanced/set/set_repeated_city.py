def is_repeated_city(num):
    my_set = set()
    for i in range(num):
        city = input()
        my_set.add(city)
    tmp_set = set()
    called_names = input()
    tmp_set.add(called_names)
    if len(my_set.union(tmp_set)) > len(my_set):
        print('OK')
    else:
        print('REPEAT')
    
num = int(input())

is_repeated_city(num)