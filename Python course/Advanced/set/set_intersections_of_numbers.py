def get_intersections_of_numbers(n):
    my_set = set()
    for i in range(n):
        number = int(input())
        tmp_my_set = set()
        while number > 0:
            last_digit = number % 10
            tmp_my_set.add(last_digit)
            number = number // 10
        if i != 0:
            my_set.intersection_update(tmp_my_set)
        else:
            my_set = tmp_my_set
    list1 = list(my_set)
    list1.sort()
    
    print(*list1)
    
n = int(input())

get_intersections_of_numbers(n)