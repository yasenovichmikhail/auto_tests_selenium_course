
def is_the_same_digit(num1, num2):
    my_set1 = set()
    my_set2 = set()
    while num1 > 0:
            last_digit = num1 % 10
            my_set1.add(last_digit)
            num1 = num1 // 10

    while num2 > 0:
            last_digit = num2 % 10
            my_set2.add(last_digit)
            num2 = num2 // 10
    if my_set1.isdisjoint(my_set2) == True:
        print('NO')
    else:
        print('YES')

num1 = 1523
num2 = 3678

is_the_same_digit(num1, num2)