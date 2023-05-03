
def is_subset(num1, num2):
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
    if my_set2.issubset(my_set1) == True:
        print('YES')
    else:
        print('NO')

num1 = 1254
num2 = 1243
is_subset(num1, num2)