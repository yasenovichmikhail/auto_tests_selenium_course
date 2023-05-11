def get_string_repres_of_number(numbers, num):
    my_list = []
    for i in numbers:
        while num > 0:
            x = num % 10
            my_list.append(numbers[x])
            num = num // 10
    result = my_list[::-1]
    print(*result)

numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 0: 'zero'}

num = 230

get_string_repres_of_number(numbers, num)

