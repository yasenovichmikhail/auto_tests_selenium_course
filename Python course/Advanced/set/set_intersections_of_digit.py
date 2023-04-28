def get_intersections_of_the_digit(n):
    my_set = set()
    while n > 0:
        last_digit = n % 10
        my_set.add(last_digit)
        n = n // 10
    print(my_set)


n = 1234567890

get_intersections_of_the_digit(n)